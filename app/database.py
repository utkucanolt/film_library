from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
load_dotenv()

# Sadece PostgreSQL bağlantısı
DATABASE_URL = os.getenv("DATABASE_URL")  # Ortam değişkeni olmak zorunda

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable is not set")

# PostgreSQL engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
