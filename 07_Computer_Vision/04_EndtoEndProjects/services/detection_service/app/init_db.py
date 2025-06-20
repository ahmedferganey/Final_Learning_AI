import os
import time
import psycopg2
from psycopg2 import sql, OperationalError
from dotenv import load_dotenv

# Load environment variables from .env file inside the container
load_dotenv(dotenv_path="/app/.env")

# Environment Variables with Fallbacks
DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "violations_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASSWORD", "postgres")

MAX_RETRIES = 10
RETRY_DELAY = 3  # seconds

# SQL for creating the violations table
CREATE_TABLE_SQL = """
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

def connect_db(dbname):
    return psycopg2.connect(
        dbname=dbname,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )

def ensure_role_and_database():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"[DB INIT] 🔄 Attempt {attempt}: Connecting to 'postgres' to verify role/database...")
            conn = connect_db("postgres")
            conn.autocommit = True
            cur = conn.cursor()

            # Create role if missing
            cur.execute("SELECT 1 FROM pg_roles WHERE rolname = %s", (DB_USER,))
            if not cur.fetchone():
                print(f"[DB INIT] 🧾 Creating role '{DB_USER}'...")
                cur.execute(
                    sql.SQL("CREATE ROLE {} WITH LOGIN SUPERUSER PASSWORD %s").format(sql.Identifier(DB_USER)),
                    (DB_PASS,)
                )

            # Create database if missing
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
            if not cur.fetchone():
                print(f"[DB INIT] 🗃️ Creating database '{DB_NAME}'...")
                cur.execute(
                    sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME))
                )

            cur.close()
            conn.close()
            print("[DB INIT] ✅ Role and database ensured.")
            break

        except OperationalError as e:
            print(f"[DB INIT] ❌ Connection failed: {e}")
            if attempt == MAX_RETRIES:
                print("[DB INIT] ❌ Giving up after max retries.")
                raise
            time.sleep(RETRY_DELAY)

def ensure_table():
    try:
        print(f"[DB INIT] 📥 Connecting to '{DB_NAME}' to create table...")
        conn = connect_db(DB_NAME)
        with conn:
            with conn.cursor() as cur:
                cur.execute(CREATE_TABLE_SQL)
        conn.close()
        print("[DB INIT] ✅ Table 'violations' ensured.")
    except Exception as e:
        print(f"[DB INIT] ❌ Failed to create table: {e}")
        raise

if __name__ == "__main__":
    ensure_role_and_database()
    ensure_table()

