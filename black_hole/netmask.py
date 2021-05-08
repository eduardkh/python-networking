import ipaddress

ip = "192.168.0.0/255.255.0.0"
# ip = "192.168.0.0/28"
net = ipaddress.ip_network(ip)
print(net.with_netmask.split("/")[0])
print(net.netmask)
