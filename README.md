# 📁 File Processing Service

A backend service built with Python and Flask that provides RESTful API endpoints for uploading, validating, and processing .txt and .csv files. This project was created as a take-home coding challenge to demonstrate best practices in API design, file handling, modularity, logging, and error handling.

**Built with:**

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white&style=for-the-badge)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-000000?logo=flask&logoColor=white&style=for-the-badge)](https://flask.palletsprojects.com/)


## ✨ Features

- ✅ **File Upload Endpoint:** Accepts `.txt` and `.csv` file uploads via a `POST` request.
- ✅ **Robust Validation:** Ensures that a file is present and has an allowed extension before processing.
- ✅ **File Processing:** Accurately counts the number of lines and words in the uploaded file content.
- ✅ **In-Memory Database Simulation:** Stores processed results (filename, line count, word count) in an in-memory dictionary for later retrieval.
- ✅ **File Information Retrieval Endpoint:** Allows clients to fetch processed data for all files or one file using a unique file ID via a `GET` request.
- ✅ **Structured Logging:** Implements comprehensive logging for key actions and errors to aid in debugging and monitoring.
- ✅ **Exception Handling:** Catches common errors (e.g., disallowed file types, file decoding errors) and returns appropriate HTTP status codes and clear error messages.


## 🔧 Project Setup

### Installation & Running the Service

1.  **Clone the Repository:**
    ```bash
    git clone  https://github.com/AzureNights/FileProcessingService.git
    cd FileProcessingService
    ```

2.  **Create and Activate a Python Virtual Environment:**
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Flask Application:**
    ```bash
    python app.py
    ```
     *Open in an API client like Postman at `http://12-7.0.0.1:5000/api/process-file`*


## 📦️ API Usage

### 1. Upload and Process a File

*   **Endpoint:** `POST /upload-file`
*   **Method:** `POST`
*   **Body:** `form-data`
    *   **Key:** `file`
    *   **Type:** File
    *   **Value:** Select a `.txt` or `.csv` file.

### 2. Retrieve All Processed Results

*  **Endpoint:** `GET /view/all`
*  **Method:** `GET`

### 3. Retrieve Processed Results for a Specific File

*  **Endpoint:** `GET /view/<id>`
*  **Method:** `GET`
  

## 💡 Design Choices

*   **Modularity & Separation of Concerns**
    *   The application is split into two primary modules: `app.py` for handling the web/API layer (Controllers) and `service.py` for the core business logic. This separation makes the code easier to understand, test, and maintain.

*   **Early Validation**
    *   File validation (checking for presence, filename, and allowed extensions) is performed immediately upon receiving a request. This approach rejects invalid requests quickly, saving system resources. `pathlib` is used for robust and modern file extension handling.

*   **Comprehensive Logging**
    *   Structured logging is implemented throughout the application using Python's standard `logging` module. This provides clear visibility into the application's flow, from receiving requests to processing and error handling, which is crucial for debugging and monitoring in a production environment.

*   **Exception Handling**
    *   A multi-layered `try-except` block in the upload endpoint handles potential errors gracefully. It catches specific, expected errors (like `UnicodeDecodeError` for non-text files) and returns a helpful `400 Bad Request`. A general `except` block catches any other unexpected server-side issues and returns a safe `500 Internal Server Error`, preventing the service from crashing.

*   **In-Memory Database Simulation**
    *   As per the challenge instructions, a simple Python dictionary is used to simulate a database for storing processed results. This approach demonstrates the core data storage and retrieval logic without the setup of a real database.
      

## 🧠 Future Improvements

To evolve this service into a production-grade application, the following steps would be considered:

*   **Persistent Database:** Replace the in-memory dictionary with a persistent database like **MySQL**.
*   **Enhanced Automated Testing:** Implement a comprehensive test suite using a framework like **pytest**. This would include:
    *   **Unit tests** for the functions in `service.py`.
    *   **Integration tests** for the Flask API endpoints to validate the full request-response cycle.
*   **Configuration Management:** Externalize settings like `ALLOWED_EXTENSIONS` into a separate configuration file (e.g., `config.py` or a `.env` file) to avoid hardcoding values.
*   **Containerization:** Dockerize the application for consistent deployments and easier scalability.
