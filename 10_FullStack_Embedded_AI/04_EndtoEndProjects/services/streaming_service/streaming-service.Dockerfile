# ============================
# 🔧 Stage 1: Base Image Setup
# ============================
FROM python:3.11-slim AS base

# Prevent .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Ensure the app folder is treated as a module
ENV PYTHONPATH=/app

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app/ ./app


# ============================
# 🚀 Final Stage
# ============================
FROM base AS final

# Expose port for FastAPI
EXPOSE 9000

# Run the app with uvicorn (faster & cleaner logs)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "9000"]

