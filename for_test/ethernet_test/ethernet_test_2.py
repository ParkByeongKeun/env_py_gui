import socket

def check_ip_collision(ip_address):
    try:
        socket.inet_aton(ip_address)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip_address, 80))
            if result == 0:
                # print(f"IP address {ip_address} is already in use. Collision detected!")
                print(ip_address)
                return True
            else:
                # print(f"IP address {ip_address} is available. No collision detected.")
                # print('good')
                return False
    except socket.error:
        print(f"Invalid IP address: {ip_address}")
        return False

# Usage example
ip_address = '192.168.0.24'  # Replace with the IP address you want to check
for i in range(1,256):
    text = '192.168.0.' + str(i)
    check_ip_collision(text)
    # print(text)
    # print(i)
# check_ip_collision(ip_address)