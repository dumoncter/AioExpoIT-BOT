from netmiko import ConnectHandler

ip = '192168'
mac_adress = ''
mac_adress2 = mac_adress.lower()
mac_adress1 = '65:65'
zywall = {
    'device_type': 'zyxel_os',
    'host': '192.168.200.1',
    'username': 'ssh_bot',
    'password': 'Ckj;ysqgfhjkm13',
    'port': 22,  # optional, defaults to 22
    'secret': '',  # optional, defaults to ''
}
commands_add_ip = [
    'configure terminal',
    f'ip dhcp pool Static_LAN1_{ip}5050',
    'show'
    # 'host 192.168.110.102'
    # 'hardware-address 00:E0:4C:68:0B:E6'
    # 'description Hueta3'
    # 'exit'
]

commands_ssh_find = [
    f'show arp-table | match "{mac_adress}"'
    # 'host 192.168.110.102'
    # 'hardware-address 00:E0:4C:68:0B:E6'
    # 'description Hueta3'
    # 'exit'
]


def ssh_add():
    net_connect = ConnectHandler(**zywall)
    output = net_connect.send_config_set(commands_add_ip)
    return output


def ssh_find_mac():
    net_connect = ConnectHandler(**zywall)
    output = net_connect.send_config_set(commands_ssh_find)
    return output.split('Router')
