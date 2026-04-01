import socket

def check_ip_availability(ip_address, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip_address, port))
        print(f"The IP address {ip_address} is already in use.")
    except ConnectionRefusedError:
        print(f"The IP address {ip_address} is available.")
    finally:
        s.close()
# 사용 예시
check_ip_availability('192.168.0.3', 80)
