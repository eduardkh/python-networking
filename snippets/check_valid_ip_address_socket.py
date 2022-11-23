import socket

ip = "111.1.1.1"

try:
    socket.inet_aton(ip)
    print(f"{ip} is valid")
except socket.error:
    print(f"{ip} is NOT valid")
