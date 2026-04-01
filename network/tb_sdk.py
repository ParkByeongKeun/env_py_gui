# pip isntall pandas
# pip install thingsboard-gateway


from thingsboard_gateway.tb_client import TBClient
from thingsboard_gateway.tb_utility.tb_utility import TBUtility

THINGSBOARD_HOST = "210.117.143.37"
# THINGSBOARD_HOST = "demo.thingsboard.io"
ACCESS_TOKEN='51ZFhNEWFXLi4pW758Gy'
port = 10061
tb_client = TBClient(THINGSBOARD_HOST, ACCESS_TOKEN)


tb_client.connect()

data = {
    "s1":1,
    "s2":1
}

payload = TBUtility.dict_to_json(data)

tb_client.send_telemetry_data(payload)

tb_client.disconnect()