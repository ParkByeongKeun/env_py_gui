# from wifi import Cell, Scheme
# import subprocess

# def get_wifi_list():
#     cells = Cell.all('wlan0')
#     for cell in cells:
#         print(cell.ssid)
    
#     try:
#         result = subprocess.check_output(["iwgetid", "-r"])
#         print("현재 연결된 WiFi의 SSID:", result.decode().strip())
#         # self.current_wifi_label.config(text=result.decode().strip())
#         for cell in cells:
#             print(cell.ssid)
#         # 여기서 gui update해줘야한다.
#     except:
#         result = ''
        
#     # self.current_wifi_label.after(1000, self.get_wifi_list)
    
# get_wifi_list()

import network
import subprocess
import re

def wifi_Search():
    wifilist = []
    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        if cell.ssid != '':
            signal = abs(cell.signal)
            if signal <= 50:
                wifilist.append([cell.ssid, 'a'])
            elif signal <= 65:
                wifilist.append([cell.ssid, 'b'])
            else:
                wifilist.append([cell.ssid, 'c'])
    
    '''
    cell.signal
                <= 50           -> Good connection strength => a
                50 < && < 65    -> SoSo connection strength => b
                65 <=           -> Bad  connection strength => c

    '''

    return wifilist

'''
IN-USE  BSSID              SSID                   MODE   CHAN  RATE        SIGNA                     L  BARS  SECURITY
        2C:D2:6B:61:C9:7C  NEXT340-ca5305         Infra  6     65 Mbit/s   100                          ▂▄▆█  WPA2
        B4:B0:24:C3:96:2E  mirresys               Infra  7     405 Mbit/s  100                          ▂▄▆█  WPA2
        B6:B0:24:A3:96:2E  --                     Infra  7     405 Mbit/s  100                          ▂▄▆█  WPA1 WPA2
        88:36:6C:FD:19:9E  DIRECT-ABOFFIEPCmsJP   Infra  7     270 Mbit/s  100                          ▂▄▆█  WPA2
        B4:B0:24:C3:96:30  mirresys               Infra  161   405 Mbit/s  90                           ▂▄▆█  WPA2
        B6:B0:24:D3:96:2E  --                     Infra  161   405 Mbit/s  90                           ▂▄▆█  WPA1 WPA2
        90:9F:33:A9:0B:8C  sangsanglab            Infra  13    405 Mbit/s  79                           ▂▄▆_  WPA2
*       90:9F:33:A8:0B:8C  sangsanglab_5G         Infra  149   405 Mbit/s  77                           ▂▄▆_  WPA2
'''

def wifi_search_new_ver():
    available_wifilist = []
    current_wifi = []
    try:
        output = subprocess.check_output(["nmcli", "dev", "wifi", "list"])
        
        output = output.decode("utf-8")
        lines = output.split("\n")
        # print(lines)
        for line in lines:
            if "SSID" not in line and "MODE" not in line and "*" not in line and line != '':
                # print('* not in line')
                wifi_info = re.findall(r"\S+", line)
                # wifi SSID가 띄워쓰기가 있으면 매우 곤란한데...
                if wifi_info[1] != '--':
                    # print('Available list')
                    # print(wifi_info[1])       # ssid
                    # print(wifi_info[6])       # signal
                    # print(wifi_info[-1])      # security
                    if wifi_info[6] == 'Mbit/s':
                        pass
                    else:
                        wifi_info[6] = int(wifi_info[6])
                        temp_grade = ''
                        if wifi_info[6] >= 80:
                            temp_grade = 'a'
                        elif wifi_info[6] >=60:
                            temp_grade = 'b'
                        elif wifi_info[6] >=40:
                            temp_grade = 'c'
                        elif wifi_info[6] <40 and wifi_info[6] >0:
                            temp_grade = 'd'
                        else:
                            temp_grade = 'e'
                            print('wifi signal error')
                    
                    
                    # available_wifilist.append([wifi_info[1], wifi_info[6], wifi_info[-1]])
                        available_wifilist.append([wifi_info[1], temp_grade, wifi_info[-1]])

            elif "*" in line:
                # Extract the Wi-Fi information from the line
                wifi_info = re.findall(r"\S+", line)
                
                # print('10:',end='')
                # print(wifi_info[9])         # <- 여기가 security인데 '--' 나오면 비번이 없는 것..? 맞을꺼야
                # print('Current list')
                # print(wifi_info[2])
                # print(wifi_info[7])
                # print(wifi_info[-1])
                # print()
                current_wifi.append([wifi_info[2], wifi_info[7], wifi_info[-1]])
                
                
                
                # return [wifi_info[2], wifi_info[-3], wifi_info[-1]]            # name & strength를 반환
                
                
                # print(wifi_info)
        return [current_wifi, available_wifilist]
    except subprocess.CalledProcessError:
        return None
    
    
def connect_non_pw_wifi(ssid):
    cmd = f"nmcli device wifi connect '{ssid}'"
    subprocess.call(cmd, shell=True)

def get_current_wifi_info():
    try:
        output = subprocess.check_output(["nmcli", "dev", "wifi", "list"])
        output = output.decode("utf-8")
        lines = output.split("\n")
        for line in lines:
            # print(line)
            if "*" in line:
                # Extract the Wi-Fi information from the line
                wifi_info = re.findall(r"\S+", line)
                # print('1:',end='')
                # print(wifi_info[0])
                # print('2:',end='')
                # print(wifi_info[1])
                # print('3:',end='')
                # print(wifi_info[2])
                # print('4:',end='')
                # print(wifi_info[3])
                # print('5:',end='')
                # print(wifi_info[4])
                # print('6:',end='')
                # print(wifi_info[5])
                # print('7:',end='')
                # print(wifi_info[6])
                # print('8:',end='')
                # print(wifi_info[7])
                # print('9:',end='')
                # print(wifi_info[8])
                # print('10:',end='')
                # print(wifi_info[9])         # <- 여기가 security인데 '--' 나오면 비번이 없는 것..? 맞을꺼야
                
                
                
                return [wifi_info[2], wifi_info[-3], wifi_info[-1]]            # name & strength를 반환
                
                
                # print(wifi_info)
    except subprocess.CalledProcessError:
        return None
def Search():
    wifilist = []

    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        wifilist.append(cell)

    return wifilist


def FindFromSearchList(ssid):
    wifilist = Search()

    for cell in wifilist:
        if cell.ssid == ssid:
            return cell

    return False


def FindFromSavedList(ssid):
    cell = wifi.Scheme.find('wlan0', ssid)

    if cell:
        return cell

    return False


def connect_wifi(ssid, password):
    cmd = 'nmcli device wifi connect {} password {}'.format(ssid, password)
    subprocess.call(cmd, shell=True)

def Connect(ssid, password=None):
    cell = FindFromSearchList(ssid)

    if cell:
        savedcell = FindFromSavedList(cell.ssid)

        # Already Saved from Setting
        if savedcell:
            savedcell.activate()
            return cell

        # First time to conenct
        else:
            if cell.encrypted:
                if password:
                    scheme = Add(cell, password)

                    try:
                        scheme.activate()

                    # Wrong Password
                    except wifi.exceptions.ConnectionError:
                        Delete(ssid)
                        return False

                    return cell
                else:
                    return False
            else:
                scheme = Add(cell)

                try:
                    scheme.activate()
                except wifi.exceptions.ConnectionError:
                    Delete(ssid)
                    return False

                return cell
    
    return False


def Add(cell, password=None):
    if not cell:
        return False

    scheme = wifi.Scheme.for_cell('wlan0', cell.ssid, cell, password)
    scheme.save()
    return scheme


def Delete(ssid):
    if not ssid:
        return False

    cell = FindFromSavedList(ssid)

    if cell:
        cell.delete()
        return True

    return False

    




# get_current_wifi_info()

'''
IN-USE  BSSID              SSID                   MODE   CHAN  RATE        SIGNA                     L  BARS  SECURITY
        2C:D2:6B:61:C9:7C  NEXT340-ca5305         Infra  6     65 Mbit/s   100                          ▂▄▆█  WPA2
        B4:B0:24:C3:96:2E  mirresys               Infra  7     405 Mbit/s  100                          ▂▄▆█  WPA2
        B6:B0:24:A3:96:2E  --                     Infra  7     405 Mbit/s  100                          ▂▄▆█  WPA1 WPA2
        88:36:6C:FD:19:9E  DIRECT-ABOFFIEPCmsJP   Infra  7     270 Mbit/s  100                          ▂▄▆█  WPA2
        B4:B0:24:C3:96:30  mirresys               Infra  161   405 Mbit/s  90                           ▂▄▆█  WPA2
        B6:B0:24:D3:96:2E  --                     Infra  161   405 Mbit/s  90                           ▂▄▆█  WPA1 WPA2
        90:9F:33:A9:0B:8C  sangsanglab            Infra  13    405 Mbit/s  79                           ▂▄▆_  WPA2
*       90:9F:33:A8:0B:8C  sangsanglab_5G         Infra  149   405 Mbit/s  77                           ▂▄▆_  WPA2
'''




########################################################################################
# ehternet or wlan notification
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

#############################

def get_current_connection_state():
    # type - dictionary
    interfaces = psutil.net_if_stats()
    # print('eth0: ',interfaces['eth0'].isup)
    # print('wlan0: ',interfaces['wlan0'].isup)

    eth0_connection = interfaces['eth0'].isup
    wlan0_connection = interfaces['wlan0'].isup
    return [eth0_connection, wlan0_connection]

# wifi_search_new_ver()

# ethernet 속성이지만 같이 쫌 삽시다!

# ethernet 속성이지만 같이 쫌 삽시다!
def set_static_ip(interface, ip_address, netmask, gateway, dns_servers, Manual):
    config_lines = [
        f'auto {interface}',
        f'iface {interface} inet static',
        f'address {ip_address}',
        f'netmask {netmask}',
        f'gateway {gateway}',
        f'dns-nameservers {dns_servers}'
    ]

    with open('/etc/network/interfaces', 'a') as config_file:
        
        config_file.truncate(0)
        if Manual == False:         # Auto
            config_file.write(basic_info + '\n')

        else:                       # Manual
            # config_file.write('\n'.join(config_lines) + '\n')
            config_file.write(basic_info + '\n')
            config_file.write('\n'.join(config_lines))
            
        print('reboot...')

# Usage example
interface = 'eth0'  # 인터페이스 이름 (일반적으로 eth0)
ip_address = '192.168.0.3'  # 고정 IP 주소
netmask = '255.255.255.0'  # 넷마스크
gateway = '192.168.0.1'  # 게이트웨이 주소
dns_servers = '8.8.8.8 8.8.4.4'  # DNS 서버 주소

basic_info = 'source /etc/network/interfaces.d/*\n# Network is managed by Network manager\nauto lo\niface lo inet loopback\n'



# set_static_ip(interface, ip_address, netmask, gateway, dns_servers)
