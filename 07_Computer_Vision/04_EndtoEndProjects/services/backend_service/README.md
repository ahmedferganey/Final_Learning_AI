# Streaming Service

Serves:
- Live annotated video stream over WebSocket
- Violation count via REST API
- Frontend UI with video + count

## Usage

```bash
docker build -t streaming_service .
docker run -p 8004:8004 -v $(pwd)/shared:/app/shared streaming_service


## Directory

streaming_service/
├── app/
│   ├── __init__.py
│   ├── main.py                    ← Entry point
│   ├── config.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── api.py                ← REST API for metadata
│   ├── streaming/
│   │   ├── __init__.py
│   │   └── websocket.py          ← WebSocket for real-time
│   ├── consumers/
│   │   └── annotated_frame_listener.py ← Consumes from RabbitMQ
│   └── utils/
│       └── video_buffer.py       ← (optional) frame caching
├── requirements.txt
├── Dockerfile
└── README.md

