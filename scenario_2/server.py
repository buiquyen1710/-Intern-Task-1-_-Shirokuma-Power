from pymodbus.server import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusServerContext, ModbusDeviceContext
import threading
import time
import psutil

# Create datastore
store = ModbusDeviceContext(
    hr=ModbusSequentialDataBlock(0, [0]*10)
)

context = ModbusServerContext(devices=store, single=True)

def update_registers():
    while True:
        cpu = int(psutil.cpu_percent())
        ram = int(psutil.virtual_memory().percent)

        context[0x00].setValues(3, 0, [cpu, ram])
        time.sleep(2)

threading.Thread(target=update_registers, daemon=True).start()

StartTcpServer(context, address=("0.0.0.0", 5020))
