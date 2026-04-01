import paho.mqtt.client as mqtt

# ThingsBoard 호스트 및 포트 설정
THINGSBOARD_HOST = "210.117.143.37"
PORT = 10061

# 접근 토큰 및 클라이언트 ID 설정
ACCESS_TOKEN = 'EU8HyxphCQ4wuhxlAp4s'
client_id = 'd19d0600-f460-11ed-97fe-477ec4188e5d'

# ThingsBoard에 연결되었을 때 실행되는 콜백 함수
def on_connect(client, userdata, flags, rc):
    print("Connected to ThingsBoard with result code " + str(rc))

    # 연결에 성공한 후, 구독할 토픽을 설정합니다.
    # 예시로 "v1/devices/me/telemetry" 토픽에 구독합니다.
    client.subscribe("v1/devices/me/telemetry")

# 메시지를 보냈을 때 실행되는 콜백 함수
def on_publish(client, userdata, mid):
    print("Message published")

# MQTT 클라이언트 생성
client = mqtt.Client(client_id=client_id)

# 연결 및 콜백 함수 설정
client.on_connect = on_connect
client.on_publish = on_publish

# ThingsBoard에 연결합니다.
client.connect(THINGSBOARD_HOST, PORT, keepalive=60)
from datetime import datetime
import math
ct = datetime.now()
ts = ct.timestamp()
ts = math.floor(ts*1000)

# 보낼 데이터를 JSON 형식으로 작성합니다.
data = {
        'ts': ts,
        'values':{
                "S_0_0":1.1,
                "S_0_1":1.1,
                "S_0_2":1.1,
                "S_0_3":1.1,
                "S_0_4":1.1,
                "S_0_5":1.1,
                "S_0_6":1.1,
                "S_0_7":1.1,
                "S_0_8":1.1,
                "S_0_9":1.1,
                "S_0_10":1.1,
                "S_0_11":1.1,
                "S_0_12":1.1,
                "S_0_13":1.1,
                "S_0_14":1.1,
                "S_0_15":1.1,
                "S_0_16":1.1,
                "ver":'1.0.0',
                }
        }
payload = str(data)

# 토픽에 데이터를 발행합니다.
# 예시로 "v1/devices/me/telemetry" 토픽에 데이터를 발행합니다.
client.publish("v1/devices/me/telemetry", payload)

# 연결을 유지하며 메시지를 처리합니다.
client.loop_forever()
