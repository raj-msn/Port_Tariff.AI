# Port_Tariff.AI:

Port_Tariff.AI is an intelligent, AI-powered API that automates the calculation of South African port tariffs directly from unstructured vessel data. Built with FastAPI and powered by Google's Gemini Pro, it provides a seamless, accurate, and developer-friendly solution for the maritime industry.

The application is containerized with Docker for easy setup and has been successfully deployed to the Render cloud platform, making it a robust and scalable solution.

https://github.com/user-attachments/assets/c9b8832a-479e-4838-8ac9-9928eb414ba7

**Live API URL**: [https://port-tariff-ai.onrender.com/](https://port-tariff-ai.onrender.com/)<br>
**Live API Docs**: [https://port-tariff-ai.onrender.com/docs](https://port-tariff-ai.onrender.com/docs)

---

## 🌟 Key Features

-   **AI-Powered Calculations**: Leverages Google Gemini to interpret unstructured vessel text and calculate tariffs based on rules extracted from the official "Port Tariff.pdf".
-   **RESTful API**: A clean, modern API built with FastAPI.
-   **Dockerized Environment**: Fully containerized for consistent, one-command local setup.
-   **Cloud Deployed**: Professionally deployed on Render for public access and scalability.
-   **Security-First AI**: LLM responses are filtered to block harmful content if any and ensure only secure, appropriate responses.
-   **Comprehensive Logging**: Detailed request, response, and calculation logging to `api.log`.
-   **Automated Testing**: Comes with a `test_api.py` script to validate the deployed or local API.
-   **Modular Architecture**: Core logic is cleanly separated into the `tariff_engine` for maintainability.
-   **Dual Interface**: Supports both a modern REST API and a legacy CLI (`main.py`).

---

## Interactive CLI Chatbot

For local development and quick testing, the project includes an interactive CLI chatbot. You can use it to directly interact with the calculation engine without going through the API.

https://github.com/user-attachments/assets/512ee13e-1a2a-4936-83a7-909fa28f7258

### How to Use

1.  **Start the chatbot:**
    ```bash
    python main.py
    ```

2.  Use the `input` command to provide the vessel data. Paste your text, then press `Ctrl+Z` (on Windows) or `Ctrl+D` (on macOS/Linux) and then Enter to submit.

3.  Use the `calculate` command to get the tariffs.

### Available Commands

-   `input`: To enter multi-line vessel data.
-   `calculate all`: Calculates all six supported tariff types.
-   `calculate [due names]`: Calculates specific dues (e.g., `calculate port dues, light dues`).
-   `available dues`: Lists all supported tariff types.
-   `debug on` / `off`: Toggles debug mode to show detailed steps from the model.
-   `help`: Shows this list of commands.
-   `quit`: Exits the chatbot.

---

## 🚀 Getting Started: Local Setup

You can run the application locally using either Docker (recommended) or a standard Python environment.

### Option 1: Docker (Recommended)

This is the fastest and most reliable way to run the application, as it mirrors the production environment.

**Prerequisites**:
- Docker & Docker Compose installed ([Download Docker Desktop](https://www.docker.com/products/docker-desktop/))
- Git installed

#### For Mac/Linux Users:

**Steps**:
1. **Clone the repository:**
    ```bash
    git clone https://github.com/raj-msn/Port_Tariff.AI.git
    cd Port_Tariff.AI
    ```

2. **Create your environment file:**
    ```bash
    cp .env.example .env
    # Edit the .env file and add your GEMINI_API_KEY
    nano .env  # or use your preferred editor
    ```

3. **Build and run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

#### For Windows Users:

**Steps**:
1. **Clone the repository:**
    ```cmd
    git clone https://github.com/raj-msn/Port_Tariff.AI.git
    cd Port_Tariff.AI
    ```

2. **Create your environment file:**
    ```cmd
    copy .env.example .env
    # Edit the .env file and add your GEMINI_API_KEY using Notepad
    notepad .env
    ```

3. **Build and run with Docker Compose:**
    ```cmd
    docker-compose up --build
    ```

#### ✅ Verify Docker Installation

After running the command, you should see output ending with:
```
northstar-web-1  | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

The application will now be running at `http://127.0.0.1:8000`.

### Option 2: Python Virtual Environment

**Prerequisites**:
- Python 3.10+ installed on your system
- Git installed

#### For Mac/Linux Users:

**Steps**:
1. **Clone the repository:**
    ```bash
    git clone https://github.com/raj-msn/Port_Tariff.AI.git
    cd Port_Tariff.AI
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
    ```bash
    cp .env.example .env
    # Edit .env file and add your GEMINI_API_KEY
    nano .env  # or use your preferred editor (vim, code, etc.)
    ```

5. **Run the FastAPI server:**
    ```bash
    uvicorn api:app --reload
    ```

#### For Windows Users:

**Steps**:
1. **Clone the repository:**
    ```cmd
    git clone https://github.com/raj-msn/Port_Tariff.AI.git
    cd Port_Tariff.AI
    ```

2. **Create and activate a virtual environment:**
    ```cmd
    python -m venv venv
    venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```cmd
    pip install -r requirements.txt
    ```

4. **Configure environment variables:**
    ```cmd
    copy .env.example .env
    # Edit .env file and add your GEMINI_API_KEY using Notepad or any text editor
    notepad .env
    ```

5. **Run the FastAPI server:**
    ```cmd
    uvicorn api:app --reload
    ```

#### ✅ Verify Installation

After running the server, you should see output similar to:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
```

Visit `http://127.0.0.1:8000/docs` to access the interactive API documentation.

---

## 🧪 Testing the API

A test script `test_api.py` is included to verify the functionality of the API endpoints. It is pre-configured to test the live Render deployment but can be easily switched to a local server.

1.  **Ensure the server is running** (either via Docker or locally).
2.  **To test the live Render API**, simply run:
    ```bash
    python test_api.py
    ```
3.  **To test your local server**, open `test_api.py` and change the `BASE_URL` to `http://localhost:8000`.

---

## 🛰️ API Documentation & Usage

The API is documented using OpenAPI (Swagger UI), which provides an interactive way to explore and test the endpoints.

**API Docs URL**:
-   **Live**: [https://port-tariff-ai.onrender.com/docs](https://port-tariff-ai.onrender.com/docs)
-   **Local**: [http://localhost:8000/docs](http://localhost:8000/docs)

⚠️ **Note**:

- IMPORTANT: Provide complete vessel details in the payload (GT, LOA, port, days alongside, etc.) - missing information will be assumed from default values in the rule book, which may not reflect your specific vessel and timeline.

- Due to AI model variability, the API may 
occasionally return incomplete results - simply retry the 
request if this occurs.

- Performance: The live API is deployed on Render's free tier. Due to this, the service may experience cold starts and can take up to **2 minute** to respond on the first request after periods of inactivity. Use the local deployment if needed. 



### Endpoints

#### 1. Health Check

-   **Endpoint**: `GET /`
-   **Description**: Checks if the API is running and available.
-   **Success Response** (`200 OK`):
    ```json
    {
      "status": "ok"
    }
    ```

#### 2. Calculate Tariffs

-   **Endpoint**: `POST /calculate-tariffs`
-   **Description**: Calculates port tariffs from unstructured vessel data.
-   **Request Body**:
    -   `vessel_info` (string): A multi-line string containing all the vessel details.
    -   `requested_dues` (list[string], optional): A list of specific dues to calculate. **If `null` or omitted, all available tariffs will be calculated.**
-   **Success Response** (`200 OK`):
    ```json
    {
      "results": {
        "Light Dues": "ZAR 60,062.04",
        "VTS Dues": "ZAR 33,345.00",
        "Running of Vessel Dues": "ZAR 3,309.12"
      }
    }
    ```

### Example API Requests


##### Mac/Linux (cURL)
```bash
curl -X POST "https://port-tariff-ai.onrender.com/calculate-tariffs" \
-H "Content-Type: application/json" \
-d '{
  "vessel_info": "Port: Durban\n\nVessel Details:\n\nGeneral\n\nVessel Name: SUDESTADA\nBuilt: 2010\nFlag: MLT - Malta\nClassification Society: Registro Italiano Navale\nCall Sign: [Not provided]\n\nMain Details\n\nLloyds / IMO No.: [Not provided]\nType: Bulk Carrier\nDWT: 93,274\nGT / NT: 51,300 / 31,192\nLOA (m): 229.2\nBeam (m): 38\nMoulded Depth (m): 20.7\nLBP: 222\nDrafts SW S / W / T (m): 14.9 / 0 / 0\nSuez GT / NT: - / 49,069\n\nCommunication\n\nE-mail: [Not provided]\nCommercial E-mail: [Not provided]\n\nDRY\n\nNumber of Holds: 7\n\nCargo Details\n\nCargo Quantity: 40,000 MT\nDays Alongside: 3.39 days\nArrival Time: 15 Nov 2024 10:12\nDeparture Time: 22 Nov 2024 13:00\n\nActivity/Operations\n\nActivity: Exporting Iron Ore\nNumber of Operations: 2",
  "requested_dues": ["Port Dues", "Light Dues", "VTS Dues"]
}'
```

##### Windows Command Prompt
```cmd
curl -X POST "https://port-tariff-ai.onrender.com/calculate-tariffs" -H "Content-Type: application/json" -d "{\"vessel_info\": \"Port: Durban\\n\\nVessel Details:\\n\\nGeneral\\n\\nVessel Name: SUDESTADA\\nBuilt: 2010\\nFlag: MLT - Malta\\nClassification Society: Registro Italiano Navale\\nCall Sign: [Not provided]\\n\\nMain Details\\n\\nLloyds / IMO No.: [Not provided]\\nType: Bulk Carrier\\nDWT: 93,274\\nGT / NT: 51,300 / 31,192\\nLOA (m): 229.2\\nBeam (m): 38\\nMoulded Depth (m): 20.7\\nLBP: 222\\nDrafts SW S / W / T (m): 14.9 / 0 / 0\\nSuez GT / NT: - / 49,069\\n\\nCommunication\\n\\nE-mail: [Not provided]\\nCommercial E-mail: [Not provided]\\n\\nDRY\\n\\nNumber of Holds: 7\\n\\nCargo Details\\n\\nCargo Quantity: 40,000 MT\\nDays Alongside: 3.39 days\\nArrival Time: 15 Nov 2024 10:12\\nDeparture Time: 22 Nov 2024 13:00\\n\\nActivity/Operations\\n\\nActivity: Exporting Iron Ore\\nNumber of Operations: 2\", \"requested_dues\": [\"Port Dues\", \"Light Dues\", \"VTS Dues\"]}"
```

##### Windows PowerShell
```powershell
$headers = @{ "Content-Type" = "application/json" }
$body = @{
    vessel_info = @"
Port: Durban

Vessel Details:

General

Vessel Name: SUDESTADA
Built: 2010
Flag: MLT - Malta
Classification Society: Registro Italiano Navale
Call Sign: [Not provided]

Main Details

Lloyds / IMO No.: [Not provided]
Type: Bulk Carrier
DWT: 93,274
GT / NT: 51,300 / 31,192
LOA (m): 229.2
Beam (m): 38
Moulded Depth (m): 20.7
LBP: 222
Drafts SW S / W / T (m): 14.9 / 0 / 0
Suez GT / NT: - / 49,069

Communication

E-mail: [Not provided]
Commercial E-mail: [Not provided]

DRY

Number of Holds: 7

Cargo Details

Cargo Quantity: 40,000 MT
Days Alongside: 3.39 days
Arrival Time: 15 Nov 2024 10:12
Departure Time: 22 Nov 2024 13:00

Activity/Operations

Activity: Exporting Iron Ore
Number of Operations: 2
"@
    requested_dues = @("Port Dues", "Light Dues", "VTS Dues")
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://port-tariff-ai.onrender.com/calculate-tariffs" -Method POST -Headers $headers -Body $body
```


**Expected Response:**
```json
{
  "results": {
    "Port Dues": "ZAR 199,371.35",
    "Light Dues": "ZAR 60,062.04",
    "VTS Dues": "ZAR 33,345.00"
  }
}
```
*The request body if `null` or omitted, all available tariffs will be calculated*

---
## ☁️ Deployment

This application is deployed on **Render** using its Docker container runtime. The deployment is automatically triggered by pushes to the `master` branch of the source GitHub repository.

-   **Platform**: Render
-   **Service Type**: Web Service
-   **Runtime**: Docker
-   **Live URL**: [https://port-tariff-ai.onrender.com](https://port-tariff-ai.onrender.com)



---

## 🏗️ Project Architecture

-   `api.py`: The main FastAPI application file. It defines endpoints, handles requests, and coordinates with the tariff engine.
-   `tariff_engine/`: The core logic package.
    -   `chatbot.py`: Contains the `PortDuesChatbot` class, which interacts with the Gemini API. It manages the rules extracted from the PDF and performs the calculations.
    -   `prompts.py`: Stores the prompt templates sent to the Gemini model for rule extraction and calculation.
    -   `constants.py`: Defines a list of all calculable `DUES_TYPES`.
-   `main.py`: A legacy entry point for a command-line chat interface (not used by the API).
-   `Dockerfile`: Defines the Docker image, installing dependencies and copying all necessary files.
-   `docker-compose.yml`: Orchestrates the local Docker setup, including port mapping and environment variable injection.
-   `Port Tariff.pdf`: The source document containing all the tariff rules and regulations.
-   `rubrics.md`: A markdown file where the AI's extracted rules from the PDF are stored (this file is generated on first run if it doesn't exist).

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
        "requested_dues": ["Light Dues", "VTS Dues", "Running of Vessel Dues"]
      }'
```

### Response

```json
{
  "results": {
    "Light Dues": "ZAR 60,062.04",
    "VTS Dues": "ZAR 33,345.00",
    "Running of Vessel Dues": "ZAR 3,309.12"
  }
}
```

The API internally re-uses the same logic as the CLI (`python main.py`), ensuring consistency.