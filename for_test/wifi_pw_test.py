import subprocess

def check_wifi_password():
    result = subprocess.run(['iwlist', 'wlan0', 'scan'], capture_output=True, text=True)
    print('\n\n\n\n\n\n\n\n')
    print('result : ', result)
    scan_output = result.stdout
    
    print('\n\n\n\n\n\n\n\n')
    print('scan_output : ', scan_output)
    
    if 'Encryption key:on' in scan_output:
        print("Wi-Fi 비밀번호가 필요합니다.")
        # 비밀번호를 입력하고 연결하는 코드를 여기에 추가합니다.
    else:
        print("Wi-Fi 비밀번호가 필요하지 않습니다.")
        # 바로 연결하는 코드를 여기에 추가합니다.

check_wifi_password()