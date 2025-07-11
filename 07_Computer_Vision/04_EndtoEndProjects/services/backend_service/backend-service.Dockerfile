# ----------------------------
# Stage 1: Builder
# ----------------------------
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies (for Pika + optional OpenCV later)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# ----------------------------
# Stage 2: Runtime
# ----------------------------
FROM python:3.10-slim

# Create app user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local /usr/local

# Copy app source code
COPY . .

# Environment setup
ENV PYTHONUNBUFFERED=1 \
    ENV=production

# Change ownership for safety
RUN chown -R appuser:appgroup /app

USER appuser

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI app with WebSocket support
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

