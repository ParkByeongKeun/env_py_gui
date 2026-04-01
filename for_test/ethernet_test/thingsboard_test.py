from datetime import datetime
from time import strftime
import json, math
import paho.mqtt.client as mqtt

from time import sleep

THINGSBOARD_HOST = "210.117.143.37"
# ACCESS_TOKEN='51ZFhNEWFXLi4pW758Gy'
port = 10061


client = mqtt.Client()
client.username_pw_set('L0Vb2jCCZSXo0kak4qGB')

try:
    client.connect(THINGSBOARD_HOST, port, 60)
    print('1')
    client.loop_start()
except Exception as e:
    print('1st Exception')
    print(e)
ct = datetime.now()
ts = ct.timestamp()
ts = math.floor(ts*1000)
sensor_data = {
    'ts': ts,
    'values': {
        "S_0_0":98.11,
        "S_0_1":96.051,
        "S_0_2":960515,
        "ver":'1.0.0'
    }
}
# ad110e80-09b9-11ee-93da-cb3ce6f56173
# L0Vb2jCCZSXo0kak4qGB
try:
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
    sleep(0.2)
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
    sleep(0.2)
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
    sleep(0.2)
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
    sleep(0.2)
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
    sleep(0.2)
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
    sleep(0.2)
    client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
    sleep(0.2)
    print('2')
except Exception as e:
    print('2nd Exception')
    print(e);
# except:
#     pass