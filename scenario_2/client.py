from pymodbus.client import ModbusTcpClient
import time

client = ModbusTcpClient("127.0.0.1", port=5020)
client.connect()

while True:
    result = client.read_holding_registers(address=0, count=2)

    if not result.isError():
        cpu = result.registers[0]
        ram = result.registers[1]
        print(f"CPU: {cpu}%  RAM: {ram}%")

    time.sleep(2)
