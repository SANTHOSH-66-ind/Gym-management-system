from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database inside data folder
DATABASE_URL = "sqlite:///./data/gym.db"

# Create connection
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# Session for database operations
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()