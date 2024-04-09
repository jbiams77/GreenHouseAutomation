import board
import digitalio
import time

# relay_pins = [
#     {'r1', board.D21},
#     {'r2', board.D20},
#     {'r3', board.D16},
#     {'r4', board.D7},
#     {'r5', board.D8},
#     {'r6', board.D25}
# ]

# for relay_pin in relay_pins.items():
#     relay = digitalio.DigitalInOut(relay_pin)
#     relay.direction = digitalio.Direction.OUTPUT


r1 = digitalio.DigitalInOut(board.D21)
r1.direction = digitalio.Direction.OUTPUT
r2 = digitalio.DigitalInOut(board.D20)
r2.direction = digitalio.Direction.OUTPUT
r3 = digitalio.DigitalInOut(board.D16)
r3.direction = digitalio.Direction.OUTPUT
r4 = digitalio.DigitalInOut(board.D7)
r4.direction = digitalio.Direction.OUTPUT
r5 = digitalio.DigitalInOut(board.D8)
r5.direction = digitalio.Direction.OUTPUT
r6 = digitalio.DigitalInOut(board.D25)
r6.direction = digitalio.Direction.OUTPUT


# for i in range(10):
#     for i in range(1, 7):
#         setattr(globals()[f'r{i}'], 'value', True)
#         time.sleep(0.1)

#     time.sleep(1)


for i in range(1, 7):
    setattr(globals()[f'r{i}'], 'value', False)
    time.sleep(0.1)
