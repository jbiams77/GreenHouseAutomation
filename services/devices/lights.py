import board
import asyncio
import logging
import datetime
import digitalio
import database.db_globals as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.enums import Controls

LOGGER = logging.getLogger(__name__)

# Database connection
engine = create_engine(db.BASE_DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class Lights:

    def __init__(self):
        self.shelf_misters = digitalio.DigitalInOut(board.D25)
        self.shelf_misters.direction = digitalio.Direction.OUTPUT
        self.on_schedule = [
            datetime.time(hour=6, minute=0, second=0)
        ]
        self.off_schedule = [
            datetime.time(hour=10, minute=0, second=0)
        ]

    async def schedule_lighting(self, time: int):
        LOGGER.info(f'Misting shelves for {time} seconds')
        self.shelf_misters.value = True
        control_entry = db.ControlsData(
            control_name=Controls.SHELF_MISTERS.value,
            control_value=True
        )
        session.add(control_entry)
        session.commit()

        await asyncio.sleep(time)

        self.shelf_misters.value = False
        control_entry = db.ControlsData(
            control_name=Controls.SHELF_MISTERS.value,
            control_value=False
        )
        session.add(control_entry)
        session.commit()
