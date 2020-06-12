import socket
host_name = socket.gethostname()
print("host_name", host_name)
host_ip = socket.gethostbyname(host_name)
print("host_ip", host_ip)

