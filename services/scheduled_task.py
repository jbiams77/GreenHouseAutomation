import datetime
from typing import Tuple
import database.db_globals as db
from database.enums import ControlActions, Days
from database.session import db_session

class ScheduledTasks:

    def __init__(self, device_name: str):
        self.device_name = device_name
        # load schedules from DB
        self.schedules = db_session.query(
                db.EventSchedule
            ).filter(
                db.EventSchedule.device_name == device_name
            ).all()

    def add_scheduled_task(self, name: str, time: datetime.time, action: ControlActions):
        scheduled_task = db.EventSchedule(
            schedule_name=name,
            device_name=self.device_name,
            action=ControlActions.ON.value,
            schedule_time=time,
            repeat_interval=Days.EVERYDAY.value,
            last_modified=datetime.datetime.now()
        )
        self.schedules.append(scheduled_task)
        db_session.add(scheduled_task)
        db_session.commit()

    def is_ready(self) -> Tuple[bool, db.EventSchedule]:
        current_time = datetime.datetime.now().time()
        for schedule in self.schedules:
            
            # Create a timedelta for the schedule time
            schedule_datetime = datetime.datetime.combine(datetime.datetime.today(), schedule.schedule_time)
            lower_bound = (schedule_datetime - datetime.timedelta(seconds=5)).time()
            upper_bound = (schedule_datetime + datetime.timedelta(seconds=5)).time()

            # Check if the current time is within the ±5 seconds window
            if lower_bound <= current_time <= upper_bound:
                return True, schedule
        return False, None

    def _get_schedule(self, name) -> db.EventSchedule:
        for schedule in self.schedules:
            if schedule.schedule_name == name:
                return schedule
        raise ValueError(f"No schedule found with name {name}")

    def _modify_schedule(self, schedule: db.EventSchedule, attr: str, value: any):
        if hasattr(schedule, attr):
            setattr(schedule, attr, value)
            schedule.last_modified = datetime.datetime.now()
            db_session.commit()
        else:
            raise ValueError(f"Schedule has no attribute {attr}")

    def update_schedule_time(self, name: str, time: datetime.time):
        schedule = self._get_schedule(name)
        self._modify_schedule(schedule, 'schedule_time', time)

    def update_schedule_action(self, name: str, action: ControlActions):
        schedule = self._get_schedule(name)
        self._modify_schedule(schedule, 'action', action.value)

    def update_schedule_intervale(self, name: str, interval: Days):
        schedule = self._get_schedule(name)
        self._modify_schedule(schedule, 'repeat_interval', interval.value)

    def get_schedule_names(self) -> list:
        return [schedule.schedule_name for schedule in self.schedules]

    def delete_device_schedules(self):
        entries_to_remove = db_session.query(db.EventSchedule).filter(db.EventSchedule.device_name == self.device_name).all()
        for entry in entries_to_remove:
            db_session.delete(entry)
        db_session.commit()

    def delete_schedules(self, name: str):
        entries_to_remove = db_session.query(db.EventSchedule).filter(db.EventSchedule.schedule_name == name).all()
        for entry in entries_to_remove:
            db_session.delete(entry)
        db_session.commit()
