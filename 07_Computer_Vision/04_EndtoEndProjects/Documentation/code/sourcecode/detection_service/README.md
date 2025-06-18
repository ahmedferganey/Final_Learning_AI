# Detection Service

Consumes frames from RabbitMQ, runs YOLOv8 inference, and stores violations locally.

## Usage

- Ensure `.env` is correctly configured.
- Run with Docker Compose or build manually.

```bash
docker build -t detection_service .
docker run --env-file .env detection_service
docker compose up --build detection_service
