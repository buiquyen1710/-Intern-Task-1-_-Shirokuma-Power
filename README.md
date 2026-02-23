# Task 1 _ Shirokuma Power

## Mô tả dự án
Dự án này triển khai một hệ thống giám sát tài nguyên hệ thống (CPU và RAM) sử dụng giao thức Modbus TCP. Bao gồm một server Modbus thu thập dữ liệu từ hệ thống và một client Modbus để đọc và hiển thị dữ liệu.

## Cấu trúc dự án
- `client_test.py`: File client test (có thể là phiên bản test của client).
- `logger_server.py`: Server logger (có thể dùng để ghi log).
- `scenario_2/`:
  - `client.py`: Client Modbus TCP để kết nối và đọc dữ liệu từ server.
  - `server.py`: Server Modbus TCP thu thập và cung cấp dữ liệu CPU và RAM.

## Yêu cầu hệ thống
- Python 3.x
- Các thư viện: pymodbus, psutil

## Cài đặt
1. Clone repository:
   ```
   git clone https://github.com/buiquyen1710/-Intern-Task-1-_-Shirokuma-Power.git
   cd -Intern-Task-1-_-Shirokuma-Power
   ```

2. Cài đặt dependencies:
   ```
   pip install pymodbus psutil
   ```

## Cách chạy
1. Chạy server:
   ```
   python scenario_2/server.py
   ```
   Server sẽ chạy trên port 5020 và cập nhật dữ liệu CPU/RAM mỗi 2 giây.

2. Chạy client (trong terminal khác):
   ```
   python scenario_2/client.py
   ```
   Client sẽ kết nối đến server và in ra phần trăm CPU và RAM mỗi 2 giây.

## Ghi chú
- Đảm bảo port 5020 không bị chặn bởi firewall.
- Server sử dụng psutil để lấy dữ liệu hệ thống thực tế.
- Client kết nối đến localhost (127.0.0.1) trên port 5020.

## Liên hệ
Nếu có câu hỏi, vui lòng tạo issue trên GitHub.