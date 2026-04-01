import subprocess
import re

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
                if wifi_info[2] != "--":
                    print('ssid : ',wifi_info[2])
                    print('signal_strength', wifi_info[-3])
                    # return ssid, bssid, mode, channel, signal_strength
                    
    except subprocess.CalledProcessError:
        return None

get_current_wifi_info()


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

