# Use official slim Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies required by OpenCV
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    ffmpeg \    
    && rm -rf /var/lib/apt/lists/*

# Copy requirements.txt first for layer caching
COPY requirements.txt .


# Upgrade pip, install NumPy 2.x and OpenCV 4.9.x
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir numpy==1.24.4 && \
    pip install --no-cache-dir opencv-python==4.9.0.80 && \
    pip install --no-cache-dir -r requirements.txt
    
# Copy the application code
COPY app ./app

# Default command to run the service
CMD ["python", "app/reader.py"]

