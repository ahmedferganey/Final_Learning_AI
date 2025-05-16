# app/db/session.py

# Import SQLAlchemy's engine creation function
# create_engine is used to establish a connection to the database
from sqlalchemy import create_engine

# Import SQLAlchemy's sessionmaker class
# sessionmaker generates new Session classes when called
from sqlalchemy.orm import sessionmaker

# Import application settings from the core config module
# Contains database configuration and other environment variables
from app.core.config import settings

# Create a database engine instance
# - settings.DATABASE_URL: Connection string from your configuration
# - echo=True: Enables SQL query logging to stdout (useful for debugging)
# This engine manages the connection pool and DBAPI interactions
#engine = create_engine(settings.DATABASE_URL, echo=True)
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Create a configured Session class
# - autocommit=False: Requires explicit commits for transactions
# - autoflush=False: Gives more control over when changes are flushed to DB
# - bind=engine: Associates this session maker with our database engine
# This will be used to instantiate individual database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()