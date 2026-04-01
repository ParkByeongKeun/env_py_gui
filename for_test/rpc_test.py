THINGSBOARD_HOST = "210.117.143.37"
ACCESS_TOKEN='51ZFhNEWFXLi4pW758Gy'
port = 10061

import paho.mqtt.client as mqtt
import os
import json

# # temp
# sensor_data = {
#         "values":{
#                 "S_0_0":0,
#                 "S_0_1":0,
#                 "S_0_2":0,
#                 "S_0_3":0,
#                 "S_0_4":0,
#                 "S_0_5":0,
#                 "S_0_6":0,
#                 "S_0_7":0,
#                 "S_0_8":0,
#                 "S_0_9":0,
#                 "S_0_10":0,
#                 "S_0_11":0,
#                 "S_0_12":0,
#                 "S_0_13":0,
#                 }}

# self.client = mqtt.Client()
#         self.client.username_pw_set(ACCESS_TOKEN)
#         self.client.connect(THINGSBOARD_HOST, port, 60)
#         self.client.loop_start()
        
        
#     def send_mqtt_data(self):

#         ct = datetime.now()
#         ts = ct.timestamp()
#         ts = math.floor(ts*1000)
#         sensor_data = {
#         'ts': ts,
#         'values':{
#                 "S_0_0":int(self.TVOC),
#                 "S_0_1":int(self.CO2),
#                 "S_0_2":int(self.PM10),
#                 "S_0_3":int(self.PM25),
#                 "S_0_4":int(self.CH2O),
#                 "S_0_5":int(self.NH3),
#                 "S_0_6":int(self.Sm),
#                 "S_0_7":int(self.CO),
#                 "S_0_8":int(self.NO2),
#                 "S_0_9":int(self.LIGHT),
#                 "S_0_10":int(self.SOUND),
#                 "S_0_11":int(self.Rn),
#                 "S_0_12":int(self.temperature),
#                 "S_0_13":int(self.humidity),
#                 }
#         }
#         print(sensor_data)
#         self.client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, port, 60)
client.loop_start()


client.subscribe('v1/devices/me/rpc/request/')