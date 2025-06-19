# ---------------------------------------------
# Stage 1: Build stage (builder)
# ---------------------------------------------
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies (OpenCV, GStreamer, FFmpeg)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgomp1 \
    libgstreamer1.0-0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    build-essential \
    ffmpeg \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# ---------------------------------------------
# Stage 2: Runtime stage
# ---------------------------------------------
FROM python:3.10-slim

# Create non-root user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

WORKDIR /app

# Copy installed packages from builder stage
COPY --from=builder /usr/local /usr/local

# Copy app code
COPY app/ app/
COPY requirements.txt .

# Set environment
ENV PYTHONUNBUFFERED=1 \
    ENV=production

# Set permissions
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Entrypoint
CMD ["python", "app/main.py"]

