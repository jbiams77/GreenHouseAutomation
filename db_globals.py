import os
from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

POSTGRES_USER = os.getenv("POSTGRES_USER", "local")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "changeMe")
POSTGRES_DB = os.getenv("POSTGRES_DB", "local")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "database")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
BASE_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@182.29.1.3:{POSTGRES_PORT}/{POSTGRES_DB}"

# Define your table model
class SensorData(Base):
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    inside_temperature = Column(Float)
    inside_humidity = Column(Float)
    outside_temperature = Column(Float)
    outside_humidity = Column(Float)
    light = Column(Boolean)
    fan = Column(Boolean)
