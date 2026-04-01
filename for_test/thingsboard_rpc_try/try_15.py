import paho.mqtt.client as mqtt

# ThingsBoard 호스트와 포트 설정
THINGSBOARD_HOST = "210.117.143.37"
PORT = 10061

# 임의 토큰
ACCESS_TOKEN = '51ZFhNEWFXLi4pW758Gy'

import json

# 임의로 잡아둠
client_id = 'd41e2660-f0a1-11ed-97fe-477ec4188e5d'

# MQTT 클라이언트 생성
client = mqtt.Client(client_id=client_id)

# connection call back <- 
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # access Good -> subscribe
    client.subscribe("v1/devices/me/rpc/request/+")

# 메시지 수신 콜백 함수 정의
def on_message(client, userdata, msg):
    # print("Received message: " + msg.topic + " " + str(msg.payload))

    print('topic : ', msg.topic)
    print('payload : ', str(msg.payload))
    
    decode_code = msg.payload.decode('utf-8')
    
        
    dict_data = json.loads(decode_code)
    # print(dict_data)
    try:
        if dict_data['method'] == 'setValue':           # 센서 보고 주기 설정
            # print('method is setValue')
            # print('params (type) : ', type(dict_data['params']))
            # print('params : ', dict_data['params'])
            # print(dict_data['params']['TIME'])
            # if dict_data['params'].key == 'Time':
            #     print(dict_data['params']['Time'])
            if dict_data['params']['TIME'] != None:
                print(dict_data['params']['TIME'])
            
        elif dict_data['method'] == 'execCmd':
            # print('method is execCmd')
            # print('params (type) : ', type(dict_data['params']))
            # print('params : ', dict_data['params'])
            # if dict_data['params'] ==
            # print(dict_data['params']['UPDATE'])
            if dict_data['params']['UPDATE'] != None:
                print('update')
            
        else:
            pass
    except:
        pass
    
    
    # print(type(payload))
#     topic :  v1/devices/me/rpc/request/9
# payload :  b'{"method":"execCmd","params":{"RESET":"ON"}}'

    # 수신한 메시지의 페이로드 확인
    # 원하는 RPC 명령을 처리하는 로직을 작성하세요.
    # print(msg.topic.startswith("v1/devices/me/rpc/request/"))
    if msg.topic.startswith("v1/devices/me/rpc/request/"):
        # RPC 메시지의 식별자 추출
        rpc_id = msg.topic[len("v1/devices/me/rpc/request/"):]

        # 예시: 'ping' RPC 메시지에 대한 응답 전송
        if msg.payload == b'ping':
            response_topic = "v1/devices/me/rpc/response/" + rpc_id
            client.publish(response_topic, "pong")

# 연결 및 메시지 수신 콜백 함수 설정
client.on_connect = on_connect
client.on_message = on_message

# ThingsBoard에 연결
client.username_pw_set(ACCESS_TOKEN)
client.connect(THINGSBOARD_HOST, PORT, 60)


from time import sleep
# 메시지 수신 대기
# client.loop_forever()
import threading
mqtt_thread = threading.Thread(target=client.loop_forever)
mqtt_thread.start()

i=0
while 1:
    i += 1
    print(i)
    sleep(1)

mqtt_thread.join()