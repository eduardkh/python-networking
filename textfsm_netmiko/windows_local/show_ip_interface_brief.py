import os
from dotenv import load_dotenv
from netmiko import ConnectHandler

# inject .env to env
load_dotenv()

username = os.environ.get('USER')
password = os.environ.get('PASSWORD')
secret = os.environ.get('SECRET')

# destination device parameters
router = {
    "device_type": "cisco_ios_telnet",
    "ip": "192.168.245.10",
    "username": username,
    "password": password,
    "secret": secret,
    "port": 23,
}

try:
    # destination device dictionary (**kwargs destructuring)
    c = ConnectHandler(**router)
    c.enable()
    interfaces = c.send_command("show ip interface brief", use_textfsm=True)
    # print(interfaces)
    # print("*"*80)
    for interface in interfaces:
        if interface['status'] == 'up':
            iface = interface['intf']
            addr = interface['ipaddr']
            print(
                f"- > interface {iface} is alive and reachable via {addr}")

    c.disconnect()
except Exception as e:
    print(e)
