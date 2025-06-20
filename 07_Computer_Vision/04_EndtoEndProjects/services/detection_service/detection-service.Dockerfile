# ---------------------------------------------
# Stage 1: Build stage (install Python packages)
# ---------------------------------------------
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies (OpenCV, etc.)
RUN apt-get update && apt-get install -y \
    git \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgomp1 \
    gcc \
    libgl1-mesa-glx \
    libpq-dev \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Clone YOLOv5 repo to use its internal loader
RUN git clone https://github.com/ultralytics/yolov5.git /app/yolov5

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && pip install --no-cache-dir -r /app/yolov5/requirements.txt

# ---------------------------------------------
# Stage 2: Runtime stage
# ---------------------------------------------
FROM python:3.10-slim

# Create a user for better security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy installed Python environment from builder
COPY --from=builder /usr/local /usr/local

# Copy YOLOv5 source code and set PYTHONPATH
COPY --from=builder /app/yolov5 /app/yolov5
ENV PYTHONPATH="${PYTHONPATH}:/app/yolov5"

# Copy your own app
COPY app/ app/
COPY models/ models/
COPY requirements.txt .

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    ENV=production

# Permissions
RUN chown -R appuser:appgroup /app

# Use non-root user
USER appuser

# Entrypoint: run DB migration, then service
CMD ["sh", "-c", "python app/init_db.py && python app/rabbitmq_consumer.py"]

