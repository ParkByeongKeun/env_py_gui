import subprocess

def check_ip_availability(ip_address):
    result = subprocess.run(['ping', '-c', '1', '-W', '1', ip_address], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    if result.returncode == 0:
        print(f"The IP address {ip_address} is already in use.")
        print('안된다!!!')
    else:
        print(f"The IP address {ip_address} is available.")
        

# 사용 예시
check_ip_availability('192.168.0.164')