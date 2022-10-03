import os
from netmiko import ConnectHandler


# for some reason can't get from .env file
os.environ["NET_TEXTFSM"] = "/usr/local/lib/python3.10/site-packages/ntc_templates/templates"

# get from .env file
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
    for interface in interfaces:
        if interface['status'] == 'up':
            iface = interface['intf']
            addr = interface['ipaddr']
            print(
                f"- > interface {iface} is alive and reachable via {addr}")

    c.disconnect()
except Exception as e:
    print(e)
