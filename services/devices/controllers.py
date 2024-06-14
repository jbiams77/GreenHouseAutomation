import board
import asyncio
import logging
import datetime
import digitalio
from database.session import db_session

from database.enums import Controls
from services.devices.relay import RelayController

LOGGER = logging.getLogger(__name__)



class Irrigation(RelayController):

    def __init__(self, device_name: str, board_pin: board):
        super().__init__(f'irrigation_{device_name}', board_pin)

    async def mist_shelves(self, duration: int):
        await super().on_duration(duration)


class Lights(RelayController):

    def __init__(self, device_name: str, board_pin: board):
        super().__init__(f'lights_{device_name}', board_pin)
