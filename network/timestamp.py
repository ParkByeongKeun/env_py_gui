import paho.mqtt.client as mqtt
import os
import json
import time
from datetime import datetime
import random
timestamp = time.time()
# timestamp = str(time.time())


print(type(timestamp))
# THINGSBOARD_HOST = "210.117.143.37"
# # THINGSBOARD_HOST = "demo.thingsboard.io"
# ACCESS_TOKEN='51ZFhNEWFXLi4pW758Gy'
# port = 10061
# sensor_data = {'my-temperature': 0, 'values':{"s1":1, "s2":2}}

# client = mqtt.Client()
# client.username_pw_set(ACCESS_TOKEN)
# client.connect(THINGSBOARD_HOST, port, 60)
# client.loop_start()

# try:
#     while True:
#         senval = random.randrange(0, 180)
#         print(senval)
#         # sensor_data['my-temperature'] = senval
    
#         client.publish('v1/devices/me/telemetry', json.dumps(sensor_data), 1)
#         time.sleep(5)
# except KeyboardInterrupt:
#     pass

# client.loop_stop()
# client.disconnect()

