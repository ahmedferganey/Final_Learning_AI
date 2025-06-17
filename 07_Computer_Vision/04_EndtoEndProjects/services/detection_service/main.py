from app.consumer import start_consuming

from app.init_db import ensure_postgres_role_and_db, ensure_violation_table

from app.config import *


# Run once before anything else
ensure_postgres_role()

if __name__ == "__main__":
    print("🚀 Starting Detection Service...")

    # Ensure DB, roles, tables
    ensure_postgres_role_and_db()
    ensure_violation_table()

    # Get model path
    model_path = os.getenv("MODEL_PATH", "app/models/yolo12m-v2.pt")

    # Make sure model file exists before continuing
    if not os.path.isfile(model_path):
        raise FileNotFoundError(f"❌ MODEL_PATH does not exist: {model_path}")
    else:
        print(f"✅ Model found at {model_path}")

    # Start consuming frames from RabbitMQ
    start_consuming()
