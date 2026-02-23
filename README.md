# Task 1 _ Shirokuma Power

## Project Description
This project implements a system resource monitoring system (CPU and RAM) using the Modbus TCP protocol. It includes a Modbus server that collects data from the system and a Modbus client to read and display the data.

## Project Structure
- `client_test.py`: Test client file (possibly a test version of the client).
- `logger_server.py`: Logger server (possibly used for logging).
- `scenario_2/`:
  - `client.py`: Modbus TCP client to connect and read data from the server.
  - `server.py`: Modbus TCP server that collects and provides CPU and RAM data.

## System Requirements
- Python 3.x
- Libraries: pymodbus, psutil

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/buiquyen1710/-Intern-Task-1-_-Shirokuma-Power.git
   cd -Intern-Task-1-_-Shirokuma-Power
   ```

2. Install dependencies:
   ```
   pip install pymodbus psutil
   ```

## Usage
1. Run the server:
   ```
   python scenario_2/server.py
   ```
   The server will run on port 5020 and update CPU/RAM data every 2 seconds.

2. Run the client (in a different terminal):
   ```
   python scenario_2/client.py
   ```
   The client will connect to the server and print CPU and RAM percentages every 2 seconds.

## Code Explanation
### server.py
This script sets up a Modbus TCP server using the pymodbus library. It creates a datastore with holding registers initialized to zeros. A background thread runs the `update_registers` function, which continuously monitors the system's CPU and RAM usage using the psutil library. Every 2 seconds, it updates the holding registers at address 0 with the current CPU percentage and RAM percentage. The server listens on all interfaces (0.0.0.0) at port 5020.

### client.py
This script acts as a Modbus TCP client. It connects to the server at localhost (127.0.0.1) on port 5020. In an infinite loop, it reads 2 holding registers starting from address 0. If the read is successful, it extracts the CPU and RAM values and prints them. The loop pauses for 2 seconds between reads to match the server's update interval.

## Notes
- Ensure port 5020 is not blocked by the firewall.
- The server uses psutil to get real system data.
- The client connects to localhost (127.0.0.1) on port 5020.

## Contact
If you have any questions, please create an issue on GitHub.