from ipaddress import IPv4Address, IPv4Network

# https://realpython.com/python-ipaddress-module/
addr_10 = IPv4Address("10.0.0.1")
addr_20 = IPv4Address("20.0.0.1")
subnet = IPv4Network("10.0.0.0/24")
print(addr_10 in subnet)
print(addr_20 in subnet)
