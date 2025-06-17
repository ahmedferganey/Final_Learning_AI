import os
import time
import psycopg2
from psycopg2 import sql, OperationalError
from dotenv import load_dotenv

# Load .env values
load_dotenv()

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = os.getenv("DB_PORT", 5432)
DB_NAME = os.getenv("DB_NAME", "violations_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")

MAX_RETRIES = 10
RETRY_DELAY = 3


def connect_db(dbname):
    return psycopg2.connect(
        dbname=dbname,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT
    )


def ensure_postgres_role_and_db():
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"🔄 Attempt {attempt}: Connecting to PostgreSQL to check role and db...")
            conn = connect_db("postgres")  # Always connect to default DB to manage roles
            conn.autocommit = True
            cur = conn.cursor()

            # Check if role exists
            cur.execute("SELECT 1 FROM pg_roles WHERE rolname = %s", (DB_USER,))
            if not cur.fetchone():
                print(f"🔧 Creating missing '{DB_USER}' role...")
                cur.execute(
                    sql.SQL("CREATE ROLE {} WITH LOGIN SUPERUSER PASSWORD %s").format(sql.Identifier(DB_USER)),
                    (DB_PASS,)
                )
            else:
                print(f"✅ Role '{DB_USER}' already exists.")

            # Check if DB exists
            cur.execute("SELECT 1 FROM pg_database WHERE datname = %s", (DB_NAME,))
            if not cur.fetchone():
                print(f"🛠️ Creating database '{DB_NAME}'...")
                cur.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(DB_NAME)))
            else:
                print(f"✅ Database '{DB_NAME}' already exists.")

            cur.close()
            conn.close()
            break

        except OperationalError as e:
            print(f"❌ Connection failed: {e}")
            if attempt == MAX_RETRIES:
                print("❌ Giving up after max retries.")
                raise
            time.sleep(RETRY_DELAY)


def ensure_violation_table():
    try:
        print(f"📥 Connecting to '{DB_NAME}' to create tables...")
        conn = connect_db(DB_NAME)
        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS violations (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            frame_path TEXT NOT NULL,
            labels TEXT[],
            bounding_boxes TEXT,
            violation_reason TEXT
        );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("✅ Table 'violations' ensured.")
    except Exception as e:
        print(f"❌ Failed to create table: {e}")
        raise


if __name__ == "__main__":
    ensure_postgres_role_and_db()
    ensure_violation_table()

