> [Demo] This is a portfolio/training scenario. NordikTech Solutions is a fictional company.

# Inventory API

A simple REST API for managing inventory items. Built with Flask, runs in Docker, and ships automatically to Docker Hub via GitHub Actions.

## Features

- `GET /` - API information
- `GET /health` - Health check
- `GET /inventory` - List all products
- `POST /inventory` - Add a new product
- In-memory storage (extendable with SQLAlchemy)
- Docker support
- CI/CD via GitHub Actions (build, test, push)

## Project Structure

.
+-- app.py
+-- test_app.py
+-- requirements.txt
+-- Dockerfile
+-- .github/
+-- workflows/
+-- ci.yml


## Requirements

- Python 3.12+
- Docker
- GitHub repository
- Docker Hub account with DOCKERHUB_USERNAME and DOCKERHUB_TOKEN stored as GitHub Secrets

## Local Development

    pip install -r requirements.txt
    python app.py

API runs at http://localhost:5000

## Docker

    docker build -t inventory-api .
    docker run -p 5000:5000 inventory-api

## Testing

    pytest -q

## CI/CD

On every push to main, the pipeline:

1. Checks out the code
2. Sets up Python
3. Installs dependencies
4. Runs tests via pytest
5. Logs in to Docker Hub
6. Builds the Docker image
7. Pushes the image to Docker Hub

## API Endpoints

GET /
Returns basic API information.

GET /health
Returns the health status.

GET /inventory
Returns all products.

POST /inventory
Adds a new product.

Request body:

    {
      "name": "Apple",
      "quantity": 10
    }

## Deployment

    docker pull rexco92/nordiktech-app:latest
