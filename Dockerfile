# =====================
# Stage 1: Builder
# =====================
FROM python:3.10-slim AS builder

WORKDIR /build

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels

# =====================
# Stage 2: Runtime
# =====================
FROM python:3.10-slim

WORKDIR /app

# Copy only built wheels
COPY --from=builder /wheels /wheels

RUN pip install --upgrade pip

RUN for whl in /wheels/*; do \
        pip install --no-cache-dir "$whl"; \
    done \
    && rm -rf /wheels

# Copy only what you need
COPY src ./src
COPY saved_models ./saved_models

EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
