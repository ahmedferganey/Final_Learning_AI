import os
from datetime import datetime
import psycopg2
from psycopg2.extras import Json
from psycopg2 import OperationalError, DatabaseError
from dotenv import load_dotenv

# Load environment variables from .env (adjust path if needed)
load_dotenv(dotenv_path="/app/.env")

class Config:
    DB_HOST = os.getenv("DB_HOST", "postgres")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_NAME = os.getenv("DB_NAME", "violations_db")
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")


class ViolationRepository:
    def __init__(self, config: Config):
        try:
            self.conn = psycopg2.connect(
                host=config.DB_HOST,
                port=config.DB_PORT,
                dbname=config.DB_NAME,
                user=config.DB_USER,
                password=config.DB_PASSWORD
            )
            print("[DB] ✅ Connection to database established.")
            self.ensure_table()  # Ensure table is created on init
        except OperationalError as e:
            print(f"[DB] ❌ Failed to connect to database: {e}")
            raise

    def ensure_table(self):
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS violations (
            id SERIAL PRIMARY KEY,
            frame_id INT NOT NULL,
            source VARCHAR(100),
            bounding_boxes JSONB NOT NULL,
            labels JSONB NOT NULL,
            timestamp TIMESTAMPTZ NOT NULL,
            frame_path TEXT,
            created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
        );
        """
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute(create_table_sql)
            print("[DB] ✅ Table 'violations' ensured.")
        except DatabaseError as e:
            print(f"[DB] ❌ Failed to create table: {e}")
            raise

    def save_violation(self, frame_id, source, bounding_boxes, labels, timestamp, frame_path):
        try:
            with self.conn:
                with self.conn.cursor() as cursor:
                    cursor.execute(
                        """
                        INSERT INTO violations (frame_id, source, bounding_boxes, labels, timestamp, frame_path, created_at)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """,
                        (frame_id, source, Json(bounding_boxes), Json(labels), timestamp, frame_path, datetime.utcnow())
                    )
                    print(f"[DB] ✅ Violation saved: Frame {frame_id} from {source}")
        except DatabaseError as e:
            print(f"[DB] ❌ Failed to save violation: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("[DB] 🔌 Connection closed.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

