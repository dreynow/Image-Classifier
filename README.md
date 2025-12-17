# Image Classification -- Serving & Deployment Focus

## Overview

This project demonstrates an **end-to-end ML serving and deployment
workflow**. Will focus more on the engineering size of things and not necessary on
a state of the art algorithm or model building.

The goal is to show **how a trained model can be packaged, served, and
orchestrated in production** using modern infrastructure tools:

-   **FastAPI** for inference serving
-   **Docker** for containerization
-   **Kubernetes** for orchestration
-   **FluxCD** for GitOps-based deployment

The model itself is intentionally simple. The real value lies in **how
it is deployed and operated**.

------------------------------------------------------------------------

## What This Project Is (and Isn't)

### ✅ This project is about:

-   Turning a trained ML model into a production API
-   Reproducible builds with Docker
-   Declarative deployment with Kubernetes
-   Continuous delivery using GitOps (FluxCD)
-   Laying foundations for GPU acceleration later

### ❌ This project is NOT about:

-   Advanced model architectures
-   Hyperparameter tuning
-   Achieving you know, state of the art accuracy

------------------------------------------------------------------------

## Architecture

    Model (.h5)
       ↓
    FastAPI Inference Service
       ↓
    Docker Container
       ↓
    Kubernetes Deployment
       ↓
    FluxCD GitOps Sync

------------------------------------------------------------------------

## Running Locally

### 1. Create environment

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Start API

``` bash
uvicorn src.app:app --host 0.0.0.0 --port 8000
```

### 3. Test inference

``` bash
curl -X POST "http://localhost:8000/predict"   -F "file=@image.jpg"
```

------------------------------------------------------------------------

### Docker

This is a multi-stage Docker file by the way. I have updated it twice before a push, so this has got two stages:

#### STAGE 1: Build
- Install compliers
- Install the Python packages
- Build wheels & artifacts etc  
Heavy lifting kinda

#### STAGE 2: Build
- Copy ONLY what’s needed to run the app
- No compilers
- No caches
- No build tools  
Lightweight kinda stuff

### Run container

``` bash
docker run -p 8000:8000 image-classifier-api
```
Test the API

``` bash
curl -X POST "http://localhost:8000/predict" -F "file=@image.jpg"
```

Open Swagger docs:

``` bash
http://localhost:8000/docs

```
