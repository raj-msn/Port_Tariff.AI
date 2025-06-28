# Port_Tariff.AI: South-African Port Tariff Calculator

Port_Tariff.AI is an intelligent, AI-powered API that automates the calculation of South African port tariffs directly from unstructured vessel data. Built with FastAPI and powered by Google's Gemini Pro, it provides a seamless, accurate, and developer-friendly solution for the maritime industry.

The application is containerized with Docker for easy setup and has been successfully deployed to the Render cloud platform, making it a robust and scalable solution.

https://github.com/user-attachments/assets/512ee13e-1a2a-4936-83a7-909fa28f7258

**Live API URL**: [https://port-tariff-ai.onrender.com/](https://port-tariff-ai.onrender.com/)<br>
**Live API Docs**: [https://port-tariff-ai.onrender.com/docs](https://port-tariff-ai.onrender.com/docs)

---

## 🌟 Key Features

-   **AI-Powered Calculations**: Leverages Google Gemini to interpret unstructured vessel text and calculate tariffs based on rules extracted from the official "Port Tariff.pdf".
-   **RESTful API**: A clean, modern API built with FastAPI.
-   **Dockerized Environment**: Fully containerized for consistent, one-command local setup.
-   **Cloud Deployed**: Professionally deployed on Render for public access and scalability.
-   **Comprehensive Logging**: Detailed request, response, and calculation logging to `api.log`.
-   **Automated Testing**: Comes with a `test_api.py` script to validate the deployed or local API.
-   **Modular Architecture**: Core logic is cleanly separated into the `tariff_engine` for maintainability.
-   **Modular Design**: Core logic is neatly separated into the `tariff_engine` package.
-   **Dual Interface**: Supports both a modern REST API and a legacy CLI (`main.py`).

---

## Interactive CLI Chatbot

For local development and quick testing, the project includes an interactive CLI chatbot. You can use it to directly interact with the calculation engine without going through the API.

*(A video demonstration of the CLI in action can be found at the top of this README.)*

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
-   Docker & Docker Compose installed.

**Steps**:
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/raj-msn/Port_Tariff.AI.git
    cd Port_Tariff.AI
    ```
2.  **Create your environment file:**
    Copy the example `.env` file and add your Gemini API key.
    ```bash
    cp .env.example .env
    # Now, edit the .env file and paste your API key
    ```
3.  **Build and run with Docker Compose:**
    ```bash
    docker-compose up --build
    ```
    The application will now be running at `http://127.0.0.1:8000`.

### Option 2: Python Virtual Environment

**Prerequisites**:
- Python 3.11+

**Steps**:
1. **Clone and set up the environment file** as described in the Docker steps.
2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the FastAPI server:**
    ```bash
    uvicorn api:app --reload
    ```
    The application will now be running at `http://127.0.0.1:8000`.

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
    -   `requested_dues` (list[string], optional): A list of specific dues to calculate. If `null` or omitted, all available tariffs will be calculated.
-   **Success Response** (`200 OK`):
    ```json
    {
      "results": {
        "Port Dues": "ZAR 199,371.35",
        "Light Dues": "ZAR 60,062.04",
        "VTS Dues": "ZAR 33,345.00"
      }
    }
    ```

### Example API Requests

#### cURL (Command Line)

This command can be run from any terminal (Git Bash, macOS, Linux).
```bash
curl -X POST "https://port-tariff-ai.onrender.com/calculate-tariffs" \
-H "Content-Type: application/json" \
-d '{
  "vessel_info": "Port: Durban\nVessel Name: SUDESTADA\nGT: 51,300\nDays Alongside: 3.39\nActivity: Exporting Iron Ore",
  "requested_dues": ["Port Dues", "Light Dues", "VTS Dues"]
}'
```

#### Windows Command Prompt

```cmd
curl -X POST "https://port-tariff-ai.onrender.com/calculate-tariffs" -H "Content-Type: application/json" -d "{\"vessel_info\": \"Port: Durban\\nVessel Name: SUDESTADA\\nGT: 51,300\\nDays Alongside: 3.39\\nActivity: Exporting Iron Ore\", \"requested_dues\": [\"Port Dues\", \"Light Dues\", \"VTS Dues\"]}"
```

#### PowerShell

```powershell
$headers = @{ "Content-Type" = "application/json" }
$body = @{
    vessel_info = @"
Port: Durban
Vessel Name: SUDESTADA
GT: 51,300
Days Alongside: 3.39
Activity: Exporting Iron Ore
"@
    requested_dues = @("Port Dues", "Light Dues", "VTS Dues")
} | ConvertTo-Json

Invoke-RestMethod -Uri "https://port-tariff-ai.onrender.com/calculate-tariffs" -Method POST -Headers $headers -Body $body
```

---

## ☁️ Deployment

This application is deployed on **Render** using its Docker container runtime. The deployment is automatically triggered by pushes to the `master` branch of the source GitHub repository.

-   **Platform**: Render
-   **Service Type**: Web Service
-   **Runtime**: Docker
-   **GitHub Repo**: [raj-msn/Port_Tariff.AI](https://github.com/raj-msn/Port_Tariff.AI)

The deployment process uses the `Dockerfile` in the root of the repository to build and run the container. The `GEMINI_API_KEY` is securely configured as an environment variable in the Render dashboard.

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