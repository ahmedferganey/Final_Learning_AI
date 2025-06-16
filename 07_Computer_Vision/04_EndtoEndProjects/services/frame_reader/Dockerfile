# Use a slim Python base image
FROM demisto/opencv:1.0.0.3252732


# Set working directory
WORKDIR /app


# Copy only requirements first, to cache dependencies if unchanged
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the app code
COPY app ./app

# Default command to run the microservice
CMD ["python", "app/reader.py"]

