from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient("127.0.0.1", port=5020)

client.connect()

result = client.read_holding_registers(address=0, count=2, device_id=1)

if not result.isError():
    print("Temperature:", result.registers[0] / 10)
    print("Humidity:", result.registers[1] / 10)
else:
    print("Read error")

client.close()
