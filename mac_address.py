# # pip3 install getmac

# import getmac

# def get_mac_address():
#     return getmac.get_mac_address()

# print(getmac.get_mac_address())
import uuid
def get_mac_address():
    a = uuid.getnode()
    mac = ':'.join(("%012X" % a)[i:i+2] for i in range(0, 12, 2))
    return mac
