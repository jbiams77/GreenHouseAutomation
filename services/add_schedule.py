import datetime
from database.enums import ControlActions, Days
import database.db_globals as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.session import db_session
from services.scheduled_task import ScheduledTasks
from database.enums import ControlActions

# add entries
# sched = db.EventSchedule(
#     schedule_name='Off',
#     device_name='lights_greenhouse',
#     action=ControlActions.OFF.value,
#     duration=5,
#     schedule_time=datetime.time(hour=22, minute=0, second=0),
#     repeat_interval=Days.EVERYDAY.value,
#     last_modified=datetime.datetime.now()
# )
# db_session.add(sched)

# sched = db.EventSchedule(
#     schedule_name='On',
#     device_name='lights_greenhouse',
#     action=ControlActions.ON.value,
#     duration=5,
#     schedule_time=datetime.time(hour=8, minute=0, second=0),
#     repeat_interval=Days.EVERYDAY.value,
#     last_modified=datetime.datetime.now()
# )
# db_session.add(sched)
# db_session.commit()

st = ScheduledTasks('lights_greenhouse')
# # st.update_schedule_time('default', datetime.time(hour=22, minute=16, second=0))
st.update_schedule_action('Off', ControlActions.OFF)
# st.delete_schedules('default', ControlActions.ON_DURATION)
