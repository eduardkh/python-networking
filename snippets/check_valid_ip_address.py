from ipaddress import ip_address

ip = "192.168.1.1"

try:
    ip_address(ip)
    print(f"{ip} - Valid IP Address")
except ValueError:
    print(f"{ip} - Invalid IP Address")
