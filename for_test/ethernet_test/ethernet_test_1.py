import subprocess

def set_ethernet_ip(interface, ip_address, subnet_mask, gateway):
    # Disable DHCP for the interface
    disable_dhcp_cmd = ['sudo', 'dhclient', '-r', interface]
    subprocess.run(disable_dhcp_cmd, check=True)

    # Set the static IP address
    set_ip_cmd = ['sudo', 'ifconfig', interface, ip_address, 'netmask', subnet_mask]
    subprocess.run(set_ip_cmd, check=True)

    # Set the default gateway
    set_gateway_cmd = ['sudo', 'route', 'add', 'default', 'gw', gateway]
    subprocess.run(set_gateway_cmd, check=True)

# Usage example
interface = 'eth0'                 # Replace with your Ethernet interface name
ip_address = '192.168.0.47'       # Replace with your desired IP address
subnet_mask = '255.255.255.0'     # Replace with your desired subnet mask
gateway = '192.168.0.1'           # Replace with your gateway IP address

set_ethernet_ip(interface, ip_address, subnet_mask, gateway)