from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Optional, Dict
import logging
import time
import uuid
import sys
import os
from contextlib import asynccontextmanager

from tariff_engine.chatbot import PortDuesChatbot
from tariff_engine.constants import DUES_TYPES

# Set console encoding to UTF-8 for Windows compatibility
if os.name == 'nt':  # Windows
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

# ---------- Logging setup ----------
# Create file handler with UTF-8 encoding
file_handler = logging.FileHandler("api.log", encoding='utf-8')
file_handler.setLevel(logging.INFO)

# Create console handler with UTF-8 encoding
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# ---------- FastAPI lifespan ----------
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info("[STARTUP] Starting Port Tariff Calculator API")
    logger.info("[INIT] Initializing chatbot instance...")
    yield
    # Shutdown
    logger.info("[SHUTDOWN] Shutting down Port Tariff Calculator API")

# ---------- FastAPI setup ----------
app = FastAPI(
    title="South-African Port Tariff Calculator",
    description="Single-endpoint API that calculates port tariffs from vessel data.",
    version="0.1.0",
    lifespan=lifespan
)

# ---------- Pydantic schema ----------
class TariffRequest(BaseModel):
    vessel_info: str
    requested_dues: Optional[List[str]] = None  # empty = all

class TariffResponse(BaseModel):
    results: Dict[str, str]  # { "Port Dues": "ZAR 199,549.22", ... }

# ---------- Request logging middleware ----------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())[:8]
    start_time = time.time()
    
    logger.info(f"[REQ] [{request_id}] {request.method} {request.url}")
    
    # Process request
    response = await call_next(request)
    
    # Log response
    process_time = time.time() - start_time
    logger.info(f"[RESP] [{request_id}] {response.status_code} - {process_time:.3f}s")
    
    return response

# ---------- Chatbot instance ----------
logger.info("[CHATBOT] Initializing PortDuesChatbot instance...")
chatbot = PortDuesChatbot()  # reused for every request
logger.info("[CHATBOT] Chatbot initialized successfully")

# ---------- Routes ----------
@app.get("/", tags=["health"])
def root():
    logger.info("[HEALTH] Health check endpoint accessed")
    return {"status": "ok"}

@app.post("/calculate-tariffs", response_model=TariffResponse, tags=["tariffs"])
def calculate_tariffs(payload: TariffRequest):
    request_id = str(uuid.uuid4())[:8]
    
    try:
        # Log request details
        vessel_lines = payload.vessel_info.split('\n')
        vessel_name = next((line for line in vessel_lines if 'Vessel Name:' in line), 'Unknown')
        port = next((line for line in vessel_lines if 'Port:' in line), 'Unknown Port')
        
        logger.info(f"[CALC] [{request_id}] Tariff calculation request:")
        logger.info(f"   > {vessel_name.strip()}")
        logger.info(f"   > {port.strip()}")
        logger.info(f"   > Requested dues: {payload.requested_dues or 'ALL'}")
        
        # 1) Set vessel data
        logger.info(f"[DATA] [{request_id}] Setting vessel data...")
        response_msg = chatbot.set_vessel_data(payload.vessel_info)
        logger.debug(f"   > {response_msg}")

        # 2) Which dues?
        dues = payload.requested_dues or DUES_TYPES
        logger.info(f"[DUES] [{request_id}] Calculating {len(dues)} due types: {', '.join(dues)}")

        # 3) Calculate
        logger.info(f"[COMPUTE] [{request_id}] Starting chatbot calculation...")
        raw_output = chatbot.calculate_specific_dues(dues)
        
        if not raw_output:
            logger.error(f"[ERROR] [{request_id}] Chatbot returned empty output")
            raise HTTPException(status_code=500, detail="Chatbot returned empty output")
        
        logger.debug(f"[OUTPUT] [{request_id}] Raw chatbot output: {raw_output[:100]}...")

        # 4) Parse results
        logger.info(f"[PARSE] [{request_id}] Parsing calculation results...")
        results: Dict[str, str] = {}
        
        if raw_output:
            for line in raw_output.splitlines():
                if "**" in line:
                    try:
                        name_part, value_part = line.split(":**")
                        name = name_part.strip("• ").strip().strip("*")
                        value = value_part.strip()
                        results[name] = value
                        logger.debug(f"   > Parsed: {name} = {value}")
                    except ValueError as e:
                        logger.warning(f"[WARN] [{request_id}] Failed to parse line: {line} - {e}")

        if not results:
            logger.error(f"[ERROR] [{request_id}] No results parsed from chatbot output")
            logger.error(f"   > Raw output: {raw_output}")
            raise HTTPException(status_code=500, detail="Unable to parse chatbot output")

        # Log successful calculation
        logger.info(f"[SUCCESS] [{request_id}] Successfully calculated {len(results)} tariffs:")
        for tariff_name, amount in results.items():
            logger.info(f"   > {tariff_name}: {amount}")

        return {"results": results}
        
    except HTTPException:
        raise  # Re-raise HTTP exceptions as-is
    except Exception as e:
        logger.error(f"[FATAL] [{request_id}] Unexpected error during calculation: {str(e)}")
        logger.exception(f"   > Full traceback:")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}") 