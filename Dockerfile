
# Stage 1: Builder
FROM python:3.10-slim AS builder

WORKDIR /build

# System deps for building wheels
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy dependency list
COPY requirements.txt .

# Upgrade pip & build wheels
RUN pip install --upgrade pip
RUN pip wheel --no-cache-dir --no-deps -r requirements.txt -w /wheels


# Stage 2: Runtime
FROM python:3.10-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY --from=builder /wheels /wheels

RUN pip install --upgrade pip && \
    for whl in /wheels/*; do \
        pip install --no-cache-dir "$whl"; \
    done && \
    rm -rf /wheels

COPY src ./src

COPY saved_models ./saved_models

RUN test -f saved_models/happy_sad/v1/model.keras


RUN addgroup --system appgroup && \
    adduser --system --ingroup appgroup appuser

USER appuser


EXPOSE 8000

CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
