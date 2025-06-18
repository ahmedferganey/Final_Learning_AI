# Use official slim Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV, GStreamer, and logging
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
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first for layer caching
COPY requirements.txt .


# Upgrade pip and install OpenCV + numpy + app dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy==1.24.4 && \
    pip install --no-cache-dir opencv-python==4.9.0.80 && \
    pip install --no-cache-dir -r requirements.txt

    
# Copy the application code
COPY app ./app


# Create necessary folders
RUN mkdir -p /app/videos /app/logs

# Environment settings
ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

# Run the reader script
CMD ["python", "app/reader.py"]
