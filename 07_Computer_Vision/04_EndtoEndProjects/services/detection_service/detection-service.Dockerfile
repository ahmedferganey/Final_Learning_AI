# ---------------------------------------------
# Stage 1: Build stage (install Python packages)
# ---------------------------------------------
FROM python:3.11-slim AS builder

WORKDIR /app

# Install system dependencies (OpenCV, PostgreSQL, etc.)
RUN apt-get update && apt-get install -y \
    git \
    wget \
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

# Install Python dependencies
COPY requirements.txt .


# Download and install FlashAttention wheel
RUN wget https://github.com/Dao-AILab/flash-attention/releases/download/v2.7.3/flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl && \
    pip install --no-cache-dir flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl && \
    rm flash_attn-2.7.3+cu11torch2.2cxx11abiFALSE-cp311-cp311-linux_x86_64.whl

# Install all other dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---------------------------------------------
# Stage 2: Runtime stage
# ---------------------------------------------
FROM python:3.11-slim

# Install runtime dependencies (OpenCV runtime libs)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

# Create a user for security
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy Python environment from builder
COPY --from=builder /usr/local /usr/local

# Copy your application code
COPY app/ app/
COPY models/ models/
COPY requirements.txt .

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    ENV=production \
    MPLCONFIGDIR=/tmp/matplotlib \
    YOLO_CONFIG_DIR=/tmp/yolo_config

# Create config directories and set permissions
RUN mkdir -p /tmp/matplotlib /tmp/yolo_config && \
    chown -R appuser:appgroup /tmp/matplotlib /tmp/yolo_config && \
    chown -R appuser:appgroup /app


# Use non-root user
USER appuser


CMD ["python", "app/rabbitmq_consumer.py"]

