import board
import asyncio
import uvicorn
import digitalio
from fastapi import FastAPI
from services import service
from services.devices.controllers import Irrigation, Lights

app = FastAPI()

# Board name = RPI name [= alias]       = pin name
# GPIO22     = D4        = pin.GPIO22   # Pin 7
# GPIO9      = D17       = pin.GPIO9    # Pin 11
# GPIO36     = D18       = pin.GPIO36   # Pin 12
# GPIO10     = D27       = pin.GPIO10   # Pin 13
# GPIO0      = D23       = pin.GPIO0    # Pin 16
# GPIO1      = D24       = pin.GPIO1    # Pin 18
# GPIO7      = D25       = pin.GPIO7    # Pin 22
# GPIO8      = D7        = pin.GPIO8    # Pin 26
# GPIO37     = D19       = pin.GPIO37   # Pin 35
# GPIO13     = D16       = pin.GPIO13   # Pin 36
# GPIO45     = D26       = pin.GPIO45   # Pin 37
# GPIO38     = D20       = pin.GPIO38   # Pin 38
# GPIO39     = D21       = pin.GPIO39   # Pin 40


shelf_misters = Irrigation('shelf_misters', board.D25)
greenhouse_lights = Lights('greenhouse', board.D20)

devices = [shelf_misters, greenhouse_lights]

@app.post("/water")
async def water_plants():
    await shelf_misters.mist_shelves(5)
    return {"status": shelf_misters.relay.value}


@app.get("/water")
def get_water_status():
    return {"status": shelf_misters.relay.value}


@app.post("/lights")
def toggle_lights():
    greenhouse_lights.toggle()
    return {"status": greenhouse_lights.relay.value}


@app.get("/lights")
def get_lights_status():
    return {"status": greenhouse_lights.relay.value}


@app.get("/schedule")
def get_lights_status():
    schedules = []
    for device in devices:
        schedules.append(device.schedules)
    return schedules


async def start_fastapi():
    config = uvicorn.Config(app, host="0.0.0.0", port=20211, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def run_concurrently():
    await asyncio.gather(
        start_fastapi(),
        service.main(devices)
    )

if __name__ == "__main__":
    asyncio.run(run_concurrently())