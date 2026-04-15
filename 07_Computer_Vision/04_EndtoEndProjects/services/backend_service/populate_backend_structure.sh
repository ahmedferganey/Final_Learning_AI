#!/bin/bash

set -e

BASE_DIR="backend_service"

echo "[+] Populating structure under existing: $BASE_DIR"

mkdir -p $BASE_DIR/app/{api/v1/endpoints,core,crud,db/models,schemas,services,sockets,streaming,utils}

# App root
cat <<EOF > $BASE_DIR/app/__init__.py
'''Init app'''
EOF

cat <<EOF > $BASE_DIR/app/main.py
from fastapi import FastAPI

from app.api.v1.endpoints import user, order, detection, health
from app.streaming import endpoints as streaming_endpoints

app = FastAPI()

app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(order.router, prefix="/api/v1/orders", tags=["orders"])
app.include_router(detection.router, prefix="/api/v1/detection", tags=["detection"])
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])
app.include_router(streaming_endpoints.router, prefix="/stream", tags=["streaming"])
EOF

# === API ===
cat <<EOF > $BASE_DIR/app/api/__init__.py
'''API package'''
EOF

cat <<EOF > $BASE_DIR/app/api/v1/__init__.py
'''API v1'''
EOF

cat <<EOF > $BASE_DIR/app/api/v1/endpoints/__init__.py
'''Endpoints'''
EOF

for f in detection order user health; do
  cat <<EOF > $BASE_DIR/app/api/v1/endpoints/${f}.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_${f}():
    return {"message": "${f} endpoint"}
EOF
done

# === Core ===
cat <<EOF > $BASE_DIR/app/core/__init__.py
'''Core'''
EOF

cat <<EOF > $BASE_DIR/app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    FIREBASE_PROJECT_ID: str = ""

    class Config:
        env_file = ".env"

settings = Settings()
EOF

cat <<EOF > $BASE_DIR/app/core/security.py
# Token validation logic goes here
EOF

cat <<EOF > $BASE_DIR/app/core/logger.py
import logging

logger = logging.getLogger("backend")
EOF

# === CRUD ===
cat <<EOF > $BASE_DIR/app/crud/__init__.py
'''CRUD init'''
EOF

for f in user order detection; do
  echo "# CRUD for $f" > "$BASE_DIR/app/crud/${f}.py"
done

# === DB ===
cat <<EOF > $BASE_DIR/app/db/__init__.py
'''DB'''
EOF

cat <<EOF > $BASE_DIR/app/db/base.py
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
EOF

cat <<EOF > $BASE_DIR/app/db/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
EOF

cat <<EOF > $BASE_DIR/app/db/init_db.py
def init():
    # Seed or initialize DB
    pass
EOF

cat <<EOF > $BASE_DIR/app/db/models/__init__.py
'''Models init'''
EOF

for f in user order detection; do
  echo "# Model for $f" > "$BASE_DIR/app/db/models/${f}.py"
done

# === Schemas ===
cat <<EOF > $BASE_DIR/app/schemas/__init__.py
'''Schemas init'''
EOF

for f in user order detection; do
  echo "# Schema for $f" > "$BASE_DIR/app/schemas/${f}.py"
done

# === Services ===
cat <<EOF > $BASE_DIR/app/services/__init__.py
'''Services init'''
EOF

for f in detection_client frame_reader_client order_processor; do
  echo "# Service: $f" > "$BASE_DIR/app/services/${f}.py"
done

# === Sockets ===
cat <<EOF > $BASE_DIR/app/sockets/__init__.py
'''Socket logic'''
EOF

cat <<EOF > $BASE_DIR/app/sockets/events.py
# WebSocket events
EOF

# === Streaming ===
cat <<EOF > $BASE_DIR/app/streaming/__init__.py
'''Streaming'''
EOF

cat <<EOF > $BASE_DIR/app/streaming/endpoints.py
from fastapi import APIRouter, WebSocket
from app.streaming.stream_handler import handle_stream

router = APIRouter()

@router.websocket("/ws")
async def stream(websocket: WebSocket):
    await handle_stream(websocket)
EOF

cat <<EOF > $BASE_DIR/app/streaming/stream_handler.py
async def handle_stream(websocket):
    await websocket.accept()
    await websocket.send_text("Streaming started")
EOF

for f in camera video_encoder manager; do
  echo "# Streaming helper: $f" > "$BASE_DIR/app/streaming/${f}.py"
done

# === Utils ===
cat <<EOF > $BASE_DIR/app/utils/__init__.py
'''Utils'''
EOF

for f in file_utils image_utils response; do
  echo "# Utility: $f" > "$BASE_DIR/app/utils/${f}.py"
done

# === Tests ===
mkdir -p $BASE_DIR/test  # ✅ ADD THIS LINE TO FIX THE ERROR

cat <<EOF > $BASE_DIR/test/__init__.py
'''Test package'''
EOF

cat <<EOF > $BASE_DIR/test/conftest.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)
EOF

for f in test_user test_order test_detection test_streaming; do
  echo "# Test: $f" > "$BASE_DIR/test/${f}.py"
done

echo "[✓] Finished populating FastAPI backend structure!"

