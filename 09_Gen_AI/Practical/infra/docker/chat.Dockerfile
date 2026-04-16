FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -e .
EXPOSE 8001
CMD ["uvicorn", "services.chat_service.app.main:app", "--host", "0.0.0.0", "--port", "8001"]
