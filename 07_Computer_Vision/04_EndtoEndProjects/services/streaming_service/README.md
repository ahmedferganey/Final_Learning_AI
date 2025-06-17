# Streaming Service

Serves:
- Live annotated video stream over WebSocket
- Violation count via REST API
- Frontend UI with video + count

## Usage

```bash
docker build -t streaming_service .
docker run -p 8004:8004 -v $(pwd)/shared:/app/shared streaming_service

