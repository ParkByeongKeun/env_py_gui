import os

def execute_cmd(cmd):
    os.system(cmd)
# ethernet 속성이지만 같이 쫌 삽시다!
def set_static_ip(interface, ip_address, netmask, gateway, dns_servers):
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
        # config_file.write('\n'.join(config_lines) + '\n')
        config_file.write(basic_info + '\n')
        config_file.write('\n'.join(config_lines))
    # execute_cmd('sudo service networking restart')
    execute_cmd('reboot')

# Usage example
interface = 'eth0'  # 인터페이스 이름 (일반적으로 eth0)
ip_address = '192.168.0.170'  # 고정 IP 주소
netmask = '255.255.255.0'  # 넷마스크
gateway = '192.168.0.1'  # 게이트웨이 주소
dns_servers = '8.8.8.8 8.8.4.4'  # DNS 서버 주소

basic_info = 'source /etc/network/interfaces.d/*\n# Network is managed by Network manager\nauto lo\niface lo inet loopback\n'



set_static_ip(interface, ip_address, netmask, gateway, dns_servers)
