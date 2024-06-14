import os
from datetime import datetime
from sqlalchemy import Column, Integer, Float, DateTime, Boolean, String, Time
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

POSTGRES_USER = os.getenv("POSTGRES_USER", "local")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "changeMe")
POSTGRES_DB = os.getenv("POSTGRES_DB", "local")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "database")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
BASE_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@182.29.1.3:{POSTGRES_PORT}/{POSTGRES_DB}"

print(BASE_DATABASE_URL)


class SensorData(Base):
    __tablename__ = 'sensor_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    inside_temperature = Column(Float)
    inside_humidity = Column(Float)
    outside_temperature = Column(Float)
    outside_humidity = Column(Float)
    light = Column(Float)
    water_in_temperature = Column(Float)
    water_out_temperature = Column(Float)


class ControlsData(Base):
    __tablename__ = 'controls_data'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.now)
    control_name = Column(String)
    control_value = Column(Boolean)


class EventSchedule(Base):
    __tablename__ = 'event_schedule'

    id = Column(Integer, primary_key=True)
    time_created = Column(DateTime, default=datetime.now)
    schedule_name = Column(String)
    device_name = Column(String)
    action = Column(String)
    duration = Column(Integer)
    schedule_time = Column(Time)
    repeat_interval = Column(String)
    last_modified = Column(DateTime)
