from enum import Enum


class Controls(Enum):
    SHELF_MISTERS = "Shelf Misters"
    GREENHOUSE_LIGHTS = "Shelf Lights"
    GREENHOUSE_FANS = "Greenhouse Fans"


class Days(Enum):
    MONDAY = "Monday"
    TUESDAY = "Tuesday"
    WEDNESDAY = "Wednesday"
    THURSDAY = "Thursday"
    FRIDAY = "Friday"
    SATURDAY = "Saturday"
    SUNDAY = "Sunday"
    EVERYDAY = "Everyday"


class ControlActions(Enum):
    ON = 'ON'
    OFF = 'OFF'
    TOGGLE = 'TOGGLE'
    TRIGGER = 'TRIGGER'
    ON_DURATION = 'ON_DURATION'
