# import subprocess
# CHANGE_STATE = False
# def get_wifi_list():
#     cmd = 'nmcli dev wifi list'
#     subprocess.call(cmd, shell=True)
#     CHANGE_STATE = True

# def connect_wifi(name, password):
#     cmd = 'nmcli device wifi connect {} password {}'.format(name, password)
#     subprocess.call(cmd, shell=True)
'''
위의 코드에서 get_wifi_list() 함수는 subprocess 모듈을 사용하여 
nmcli dev wifi list 명령을 실행하고 있습니다. 
이 명령은 Wi-Fi 네트워크 목록을 출력하는 명령어이기 때문에, 
출력된 결과를 확인하려면 함수가 완료될 때까지 기다려야 합니다.

따라서, subprocess.call() 대신에 subprocess.check_output()을 사용하여 
명령 실행 결과를 반환받도록 수정하면 됩니다. 
또한, connect_wifi() 함수를 호출하기 전에 Wi-Fi 네트워크 목록을 출력하도록 하기 위해서는 
get_wifi_list() 함수의 실행 결과를 변수에 저장한 후, 그 결과를 출력하면 됩니다.

아래는 수정된 코드입니다. => KDH 재수정
'''
import subprocess
def get_wifi_list():
    cmd = 'nmcli dev wifi list'
    subprocess.check_output(cmd, shell=True)            # 아 


def connect_wifi(name, password):
    cmd = 'nmcli device wifi connect {} password {}'.format(name, password)
    subprocess.call(cmd, shell=True)

def get_current_wifi():
    cmd = 'iwconfig wlan0'
    subprocess.call(cmd,shell=True)
import wifi
# get_wifi_list()
# connect_wifi('sangsanglab', '0327107179')
# get_current_wifi()
# print(get_wifi_list())

'''
#####################################################################################
The Wi-Fi card on your Linux PC can't connect to the internet unless it's enabled. 
To see the status of all your network interfaces, use this command:

# nmcli dev status

#####################################################################################
If you don't know the name of your Wi-Fi access point, otherwise known as the SSID, 
you can find it by scanning for nearby Wi-Fi networks.

# nmcli dev wifi list

#####################################################################################
Replace network-ssid with the name of your network. 
If you have WEP or WPA security on your WI-Fi, 
you can specify the network password in the command as well.

# nmcli dev wifi connect "network-ssid" password "network-password"
'''


'''
[['olleh_GiGA_WiFi_05A8', -52], ['olleh_WiFi_05A8', -40], ['U+NetF230', -67], 
 ['AT_410_AFAN_910604_WW_ee0e', -49], ['AP-408-701', -50], ['U+Net479C', -62]
// Good (Green)
 00:07:89:30:05:AB  olleh_WiFi_05A8             Infra  4     130 Mbit/s>   -40
40:B0:34:58:ED:74  DIRECT-76-HP OfficeJet 7510  Infra  4     65 Mbit/s >    
64:CB:E9:3F:EE:0E  AT_410_AFAN_910604_WW_ee0e   Infra  11    65 Mbit/s >    -49
E8:54:84:14:34:7C  AP-408-701                   Infra  5     270 Mbit/s>    -50
// Soso (Yellow)
00:07:89:30:05:AC  olleh_GiGA_WiFi_05A8         Infra  149   270 Mbit/s>    -52
08:5D:DD:84:47:9B  U+Net479C                    Infra  10    130 Mbit/s>    -62
// Bad (PInk)
08:5D:DD:AC:F2:2F  U+NetF230                    Infra  9     130 Mbit/s>    -67
'''


