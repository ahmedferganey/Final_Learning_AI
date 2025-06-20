## db.py
# app/db.py
import os
import json
import psycopg2
from psycopg2.extras import Json
from dotenv import load_dotenv
from datetime import datetime

load_dotenv(dotenv_path="/app/.env")

DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "violations_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)
cursor = conn.cursor()

def save_violation_record(frame_id, source, bounding_boxes, labels, timestamp, frame_path):
    try:
        cursor.execute(
            """
            INSERT INTO violations (frame_id, source, bounding_boxes, labels, timestamp, frame_path, created_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (
                frame_id,
                source,
                Json(bounding_boxes),
                Json(labels),
                timestamp,
                frame_path,
                datetime.utcnow()
            )
        )
        conn.commit()
        print(f"[DB] ✅ Violation saved: Frame {frame_id} from {source}")
    except Exception as e:
        conn.rollback()
        print(f"[DB] ❌ Failed to save violation: {e}")
