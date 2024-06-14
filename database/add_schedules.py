import datetime
from database.enums import ControlActions, Days
import database.db_globals as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Database connection
engine = create_engine(db.BASE_DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

scheduled_task = db.EventSchedule(
    schedule_name='second mist',
    device_name='ShelfIrrigation',
    action=ControlActions.ON.value,
    duration=5,
    schedule_time=datetime.time(hour=8, minute=0, second=0),
    repeat_interval=Days.EVERYDAY.value,
    last_modified=datetime.datetime.now()
)
session.add(scheduled_task)
session.commit()
