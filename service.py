import time
import board
import logging
import datetime
import digitalio
import adafruit_dht
import db_globals as db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Configure logging to output to STDOUT
logging.basicConfig(level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# Database connection
engine = create_engine(db.BASE_DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Define the pin the DHT sensor is connected to
dht_pin_1 = board.D19
dht_pin_2 = board.D22

# Initialize the DHT sensor
dht_sensor_1 = adafruit_dht.DHT22(dht_pin_1)
dht_sensor_2 = adafruit_dht.DHT22(dht_pin_2)

# light relay pin
light = digitalio.DigitalInOut(board.D20)
light.direction = digitalio.Direction.OUTPUT
light.value = False

# fan relay pin
fan = digitalio.DigitalInOut(board.D16)
fan.direction = digitalio.Direction.OUTPUT
fan.value = False
fan_threshold = 75.0

time_on = datetime.time(hour=6, minute=0, second=0)
time_off = datetime.time(hour=22, minute=0, second=0)


def get_readings():
    try:
        while True:
            # Attempt to read the temperature and humidity from the sensor
            inside_temperature = ( dht_sensor_2.temperature * (9.0 / 5.0)) + 32
            inside_humidity = dht_sensor_2.humidity

            outside_temperature = ( dht_sensor_1.temperature * (9.0 / 5.0)) + 32
            outside_humidity = dht_sensor_1.humidity

            time_now =datetime.datetime.now().time()
            light.value = time_now < time_off and time_now > time_on
            fan.value = inside_temperature > fan_threshold

            new_data = db.SensorData(
                timestamp=datetime.datetime.now(),
                inside_temperature=inside_temperature,
                inside_humidity=inside_humidity,
                outside_temperature=outside_temperature,
                outside_humidity=outside_humidity,
                light=light.value,
                fan=fan.value
            )

            # Add the new record to the session
            session.add(new_data)

            # Commit the session to save the changes to the database
            session.commit()

            # Print the temperature and humidity
            LOGGER.info("Inside Temperature: {:.1f}°F, Humidity: {:.1f}%".format(inside_temperature, inside_humidity))
            LOGGER.info("Ouside Temperature: {:.1f}°F, Humidity: {:.1f}%".format(outside_temperature, outside_humidity))

            # Wait for a few seconds before reading again
            time.sleep(30)
    except RuntimeError as error:
        LOGGER.warning(f'ERROR: {error}')
        time.sleep(2.0)
        get_readings()
    except KeyboardInterrupt:
        LOGGER.info("Exiting...")

get_readings()
