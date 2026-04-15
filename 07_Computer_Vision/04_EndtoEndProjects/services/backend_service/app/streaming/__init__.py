# File: app/streaming/__init__.py

from app.streaming.manager import WebSocketBroadcaster

# Shared global broadcaster instance
broadcaster = WebSocketBroadcaster()
