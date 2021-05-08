import os
from dotenv import load_dotenv
from netmiko import ConnectHandler
import ipaddress
import pprint

# using .env file to import credentials and device IP
load_dotenv()
user = os.environ.get('DEVICE_USERNAME')
password = os.environ.get('DEVICE_PASSWORD')
secret = os.environ.get('DEVICE_SECRET')
ip = os.environ.get('DEVICE_IP')

# device info for netmiko
router = {
    'device_type': 'cisco_ios_telnet',
    'ip': ip,
    'username': user,
    'password': password,
    'secret': secret,
    'port': 23
}

present_networks = []
user_input = input(
    "enter a network (CIDR or netmask) to throw to trash (null0)\n")
# proccess user input as IP address
net = ipaddress.ip_network(user_input)
network = net.with_netmask.split("/")[0]
netmask = net.netmask

try:
    c = ConnectHandler(**router)

    # getting the routes as a python dict
    route = c.send_command('show ip route', use_textfsm=True)
    # pprint.pprint(route)
    for i in route:
        if i['nexthop_if'] == 'Null0':
            present_networks.append(f"{i['network']}/{i['mask']}")

    # adding the routes to the device
    if str(net) not in present_networks:
        print(f"adding route {net} to blacklist")
        c.config_mode()
        add_route = c.send_config_set(
            [f"ip route {network} {netmask} Null0"])
        print(f"route {net} added to blacklist")

    else:
        print(f"route {net} already in blacklist")
except Exception as e:
    print(e)
