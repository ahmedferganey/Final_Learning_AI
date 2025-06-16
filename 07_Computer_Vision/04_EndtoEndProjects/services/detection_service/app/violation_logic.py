import os
import json
import cv2
from datetime import datetime
import psycopg2
import requests

# === Load environment variables ===
VIOLATION_SAVE_DIR = os.getenv("OUTPUT_PATH", "/processed_frames")
STREAMING_SERVICE_URL = os.getenv("STREAMING_SERVICE_URL", "http://streaming_service:8000/violation")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "violations_db")
print("[ENV] DB_NAME:", DB_NAME)  # Debug line to verify the DB name is correct

#DB_NAME = os.environ["DB_NAME"]
DB_USER = os.getenv("DB_USER", "admin")
DB_PASS = os.getenv("DB_PASS", "adminpass")

# === Directories and metadata ===
VIOLATION_DIR = os.path.join(VIOLATION_SAVE_DIR, "violations")
os.makedirs(VIOLATION_DIR, exist_ok=True)

metadata_file = os.path.join(VIOLATION_SAVE_DIR, "metadata.json")
if not os.path.exists(metadata_file):
    with open(metadata_file, "w") as f:
        json.dump({"violations": []}, f)

# === Save violation to PostgreSQL DB ===
def save_violation_to_db(timestamp, labels, image_path):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS violations (
                id SERIAL PRIMARY KEY,
                timestamp TEXT,
                labels TEXT,
                violation BOOLEAN,
                image_path TEXT
            );
        """)
        cur.execute("""
            INSERT INTO violations (timestamp, labels, image_path)
            VALUES (%s, %s, %s);
        """, (timestamp, ','.join(labels), image_path))
        conn.commit()
        cur.close()
        conn.close()
        print("[INFO] Violation saved to DB.")
    except Exception as e:
        print("[DB ERROR]", e)

# === Send violation to streaming service ===
def send_to_streaming_service(payload):
    try:
        response = requests.post(STREAMING_SERVICE_URL, json=payload)
        if response.status_code != 200:
            print(f"[STREAM ERROR] {response.status_code}: {response.text}")
    except Exception as e:
        print("[STREAMING ERROR]", e)

# === Main violation check ===
def check_violation(frame, detections):
    height, width, _ = frame.shape
    x1, y1 = int(0.05 * width), int(0.35 * height)
    x2, y2 = int(0.55 * width), int(0.95 * height)

    relevant_detections = []
    for det in detections:
        box = det['box']
        cx, cy = (box[0] + box[2]) // 2, (box[1] + box[3]) // 2
        if x1 <= cx <= x2 and y1 <= cy <= y2:
            relevant_detections.append(det)

    labels = [d['label'] for d in relevant_detections]
    if "hand" in labels and "protein" in labels and "scooper" not in labels:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_path = os.path.join(VIOLATION_DIR, f"violation_{timestamp}.jpg")
        cv2.imwrite(image_path, frame)

        # Save to metadata JSON
        with open(metadata_file, "r+") as f:
            metadata = json.load(f)
            metadata["violations"].append({
                "timestamp": timestamp,
                "labels": labels,
                "violation": True,
                "image_path": image_path
            })
            f.seek(0)
            json.dump(metadata, f, indent=4)

        # Save to DB
        save_violation_to_db(timestamp, labels, image_path)

        # Send to Streaming Service
        send_to_streaming_service({
            "timestamp": timestamp,
            "labels": labels,
            "violation": True,
            "image_path": image_path
        })

