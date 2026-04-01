import subprocess

def check_ip_availability(ip_address):
    try:
        result = subprocess.run(['ping', '-c', '1', ip_address], capture_output=True, text=True, timeout=2)
        if result.returncode == 0:
            print(f"The IP address {ip_address} is currently in use.")
        else:
            print(f"The IP address {ip_address} is available.")
            pass
    except subprocess.TimeoutExpired:
        print(f"The IP address {ip_address} is not responding.")
    except Exception as e:
        print(f"An error occurred while checking the IP address: {e}")

# Usage example
# ip_address = '192.168.0.100'  # Replace with the IP address you want to check
# check_ip_availability(ip_address)
# for i in range(1, 257):
#     ip_address = '192.168.0.' + str(i)
#     check_ip_availability(ip_address=ip_address)
    
check_ip_availability('192.168.0.24')
check_ip_availability('192.168.0.25')
check_ip_availability('192.168.0.26')