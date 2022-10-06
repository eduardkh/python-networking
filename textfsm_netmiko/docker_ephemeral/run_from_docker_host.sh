# setup p2p on linux host
sudo ip addr add 192.168.245.12/24 dev eth3
sudo ip link set up eth3
ping 192.168.245.10 -I eth3

# run the command
docker run  -ti --rm --env-file .env --volume $(pwd)/show_ip_interface_brief.py:/show_ip_interface_brief.py demisto/netmiko:1.0.0.34185 python /show_ip_interface_brief.py