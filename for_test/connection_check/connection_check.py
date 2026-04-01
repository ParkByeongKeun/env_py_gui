import psutil

# def check_network_connection():
#     """Check if Ethernet or Wi-Fi is connected"""
#     interfaces = psutil.net_if_stats()
#     print(interfaces)
#     for interface, stats in interfaces.items():
#         if interface == 'lo':  # skip localhost
#             continue
#         if stats.isup and (interface.startswith('en') or interface.startswith('eth') or interface.startswith('wlan')):
#             return True
#     return False

# # Example usage
# if check_network_connection():
#     print("Network is connected")
# else:
#     print("Network is disconnected")

interfaces = psutil.net_if_stats()
# type - dictionary

print('eth0: ',interfaces['eth0'].isup)
print('wlan0: ',interfaces['wlan0'].isup)

