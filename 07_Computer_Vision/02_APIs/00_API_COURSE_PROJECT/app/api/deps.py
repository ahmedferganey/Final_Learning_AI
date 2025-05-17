from typing import Generator
from app.db.session import SessionLocal

# Dependency for database session
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
