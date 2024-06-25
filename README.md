# Project Overview

This project consists of two microservices that have been dockerized and are designed to interact with each other:

1. **Upload Service**: Handles file uploads and stores them locally.
2. **Preprocess Service**: Processes the uploaded files.

## Directory Structure

```
project-root/
│
├── upload-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── uploads/ (directory for storing uploaded files)
│   └── logs/ (directory for storing logs)
│
├── preprocess-service/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── logs/ (directory for storing logs)
│
├── docker-compose.yml
└── .env
```

## Upload Service

### Description
The Upload Service is responsible for handling file uploads. It accepts PDF files and stores them in a local directory (`uploads`). It logs the activities in a logs directory (`logs`).

### Key Points
- **Endpoint**: `/uploadfile`
- **Methods**: `POST`
- **Logging**: Logs activities to `logs/app.log`
- **Storage**: Stores uploaded files in the `uploads` directory.

## Preprocess Service

### Description
The Preprocess Service takes the uploaded files from the Upload Service and processes them. This service will look into the `uploads` directory for files to process and log its activities in the `logs` directory.

### Key Points
- **Endpoint**: `/preprocess`
- **Methods**: `POST`
- **Logging**: Logs activities to `logs/app.log`
- **Functionality**: Processes files from the `uploads` directory.

## Dockerization

Both services are containerized using Docker. Each service has its own Dockerfile that sets up the required environment and dependencies.

### Dockerfile for Upload Service

```dockerfile
# upload-service/Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```

### Dockerfile for Preprocess Service

```dockerfile
# preprocess-service/Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]
```
1. **Upload a File**:
   Use a tool like Postman to send a POST request to `http://localhost:5001/uploadfile` with a file.

2. **Preprocess the File**:
   The preprocess service at this moment is a placeholder, it will be replaced as and when the preprocessing is decided as it might require certain hardcoding.

## Communication Between Services

The services use Docker's default bridge network to communicate. The Upload Service makes the uploaded files available in the `uploads` directory, which is shared with the Preprocess Service via a Docker volume. This allows the Preprocess Service to access and process the files uploaded by the Upload Service.

## Logging

Both services log their activities to log files located in the `logs` directory. This directory is mounted as a Docker volume, ensuring that logs are persistent and accessible across both services.
