import random
import time
import threading

from pymodbus.server import StartTcpServer
from pymodbus.datastore import (
    ModbusSequentialDataBlock,
    ModbusServerContext,
    ModbusDeviceContext,
)

store = ModbusDeviceContext(
    hr=ModbusSequentialDataBlock(0, [0]*10)
)

context = ModbusServerContext(devices=store, single=True)

def update_data():
    while True:
        temperature = random.randint(200, 350)
        humidity = random.randint(400, 700)

        context[0x00].setValues(3, 0, [temperature, humidity])
        time.sleep(2)

thread = threading.Thread(target=update_data)
thread.daemon = True
thread.start()

print("Smart Logger running on port 5020")
StartTcpServer(context, address=("0.0.0.0", 5020))
