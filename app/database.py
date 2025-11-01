from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# ---------------------------------------------------
# ⚙️  Direct Database URL (edit your credentials below)
# ---------------------------------------------------

<<<<<<< HEAD
import os
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
=======
load_dotenv()
>>>>>>> 3e5c3fe (Updated database.py to use .env and added .gitignore)

DATABASE_URL = os.getenv("DATABASE_URL")
# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model
Base = declarative_base()

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
