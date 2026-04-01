import subprocess

def get_current_wifi_info():
    if subprocess.run(['netsh', 'wlan', 'show', 'interface'], capture_output=True).returncode == 0:
        output = subprocess.run(['netsh', 'wlan', 'show', 'interface'], capture_output=True).stdout.decode()
        lines = output.split('\n')
        ssid = None
        key_present = False
        for line in lines:
            if 'SSID' in line:
                ssid = line.split(': ')[1].strip()
            if '인증' in line and 'WPA2-Personal' in line:
                key_present = True
        if ssid:
            print(f"현재 연결된 Wi-Fi 네트워크: {ssid}")
            if key_present:
                print("Wi-Fi 비밀번호가 걸려 있습니다.")
            else:
                print("Wi-Fi 비밀번호가 걸려 있지 않습니다.")
        else:
            print("현재 Wi-Fi에 연결되어 있지 않습니다.")
    else:
        print("Wi-Fi 정보를 가져오는 데 실패했습니다.")

get_current_wifi_info()
