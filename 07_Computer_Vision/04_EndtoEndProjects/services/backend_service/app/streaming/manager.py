# manager.py
from typing import Dict, Set
from fastapi import WebSocket
from collections import defaultdict

class StreamManager:
    def __init__(self):
        self.active_connections: Dict[str, Set[WebSocket]] = defaultdict(set)

    async def connect(self, websocket: WebSocket, camera_id: str):
        await websocket.accept()
        self.active_connections[camera_id].add(websocket)

    def disconnect(self, websocket: WebSocket, camera_id: str):
        self.active_connections[camera_id].discard(websocket)

    async def broadcast(self, camera_id: str, frame_data: bytes):
        connections = self.active_connections.get(camera_id, set())
        for connection in list(connections):
            try:
                await connection.send_bytes(frame_data)
            except Exception:
                self.disconnect(connection, camera_id)

stream_manager = StreamManager()

