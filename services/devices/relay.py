from enum import Enum
import logging
import board
import asyncio
import digitalio

from services.scheduled_task import ScheduledTasks
from database.session import db_session
import database.db_globals as db
from database.enums import ControlActions

LOGGER = logging.getLogger(__name__)


class RelayController(ScheduledTasks):

    def __init__(self, device_name: str, board_pin: board):
        super().__init__(device_name)
        self.relay = digitalio.DigitalInOut(board_pin)
        self.relay.direction = digitalio.Direction.OUTPUT

    async def run(self):
        while True:
            ready, schedule = self.is_ready()
            if ready:
                await self.action(schedule)
            await asyncio.sleep(1)

    async def action(self, schedule: db.EventSchedule):
        LOGGER.info(f'Running {schedule.action} on {self.device_name}')
        match ControlActions[schedule.action]:
            case ControlActions.ON:
                self.set_relay_and_log(True)
            case ControlActions.OFF:
                self.set_relay_and_log(False)
            case ControlActions.TOGGLE:
                self.toggle()
            case ControlActions.ON_DURATION:
                await self.on_duration(schedule.duration)

    def toggle(self):
        self.set_relay_and_log(not self.relay.value)

    async def on_duration(self, duration: int):
        self.set_relay_and_log(True)
        await asyncio.sleep(duration)
        self.set_relay_and_log(False)

    def set_relay_and_log(self, value: bool):
        self.relay.value = value
        control_entry = db.ControlsData(
            control_name=self.device_name,
            control_value=value
        )
        db_session.add(control_entry)
        db_session.commit()
