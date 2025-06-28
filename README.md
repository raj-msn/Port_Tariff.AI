# Port Tariff Calculator API

This project provides a robust API to automatically calculate South African port tariffs from unstructured vessel data. It is built with FastAPI, containerized with Docker, and uses a Gemini-powered core engine for the calculations.

## Key Features

-   **Simple API**: A single, powerful `POST /calculate-tariffs` endpoint.
-   **Dockerized**: Run the entire application with a single `docker-compose` command.
-   **Automated Testing**: Includes a `test_api.py` script to validate the API.
-   **Modular Design**: Core logic is neatly separated into the `tariff_engine` package.
-   **Dual Interface**: Supports both a modern REST API and a legacy CLI (`main.py`).

---

## 🚀 How to Run (Docker - Recommended)

This is the fastest and most reliable way to get started.

**Prerequisites:**
-   Docker & Docker Compose
-   A configured `.env` file (see **Configuration** below).

**Command:**
```bash
docker-compose up --build
```
The API will be running at `http://127.0.0.1:8000`. You can access the interactive OpenAPI docs at `http://127.0.0.1:8000/docs`.

---

## 🛠️ Local Development Setup

**1. Configuration:**
   Create a `.env` file from the example and add your Gemini API key.
   ```bash
   cp .env.example .env
   # Now, edit .env to add your key
   ```

**2. Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

**3. Run the Server:**
   ```bash
   uvicorn api:app --reload
   ```

---

## 🧪 Testing the API

Ensure the API server is running (either via Docker or locally). Then, run the test script:
```bash
python test_api.py
```
This script validates the health check and calculation endpoints.

---

## API Usage Example

Send a `POST` request to `/calculate-tariffs` with the vessel data.

**`curl` Command:**
```bash
curl -X POST "http://127.0.0.1:8000/calculate-tariffs" \
  -H "Content-Type: application/json" \
  -d '{
        "vessel_info": "Vessel Name: SUDESTADA\nGT: 51300\nLOA: 229.2\nDays Alongside: 3.39\nPort: Durban",
        "requested_dues": ["Port Dues", "Light Dues"]
      }'
```

**Success Response:**
```json
{
  "results": {
    "Port Dues": "ZAR 199,371.35",
    "Light Dues": "ZAR 60,062.04"
  }
}
```

---

## Project Structure Overview

-   `api.py`: FastAPI application, routes, and main logic.
-   `tariff_engine/`: Core package for the calculation engine (`chatbot.py`).
-   `main.py`: Legacy command-line interface.
-   `test_api.py`: API functional test script.
-   `Dockerfile` / `docker-compose.yml`: Docker configuration.
-   `Port Tariff.pdf`: The source document for tariff rules.
-   `requirements.txt`: Python dependencies.
-   `.env.example`: Template for environment variables.

## Logging

The API includes comprehensive logging:
- All requests and responses are logged with unique request IDs
- Detailed calculation steps and results are tracked
- Logs are written to both console and `api.log` file (UTF-8 encoded)
- Different log levels for debugging and production use
- Windows-compatible text symbols (no emoji issues)

### Example request

```bash
curl -X POST "http://127.0.0.1:8000/calculate-tariffs" \
  -H "Content-Type: application/json" \
  -d '{ 
        "vessel_info": "Vessel Name: SUDESTADA\nGT: 51300\nLOA: 229.2\nDays Alongside: 3.39\nPort: Durban",
        "requested_dues": ["Port Dues", "Light Dues", "Pilotage Dues"]
      }'
```

### Response

```json
{
  "results": {
    "Port Dues": "ZAR 199,549.22",
    "Light Dues": "ZAR 60,062.04",
    "Pilotage Dues": "ZAR 47,189.94"
  }
}
```

The API internally re-uses the same logic as the CLI (`python main.py`), ensuring consistency. 