import subprocess
import re

def get_network_ips():
    ip_addresses = []

    # Define the network range
    network_range = "192.168.1."

    # Ping each IP address in the network range
    for i in range(1, 255):
        ip = network_range + str(i)
        response = subprocess.Popen(['ping', '-n', '1', '-w', '500', ip], stdout=subprocess.PIPE).communicate()[0]

        # Check if the IP address is active (responded to the ping)
        if "Reply from" in response.decode():
            ip_addresses.append(ip)

    return ip_addresses

# Usage
network_ips = get_network_ips()
for ip in network_ips:
    print(ip)