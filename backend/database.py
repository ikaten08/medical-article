# backend/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database in the project root (for MVP). For production swap to Postgres.
SQLITE_DB_PATH = os.getenv("SQLITE_DB_PATH", "./medlearn.db")
engine = create_engine(f"sqlite+pysqlite:///{SQLITE_DB_PATH}", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False, future=True)

Base = declarative_base()

def get_db():
    """Dependency for FastAPI routes to get a DB session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
