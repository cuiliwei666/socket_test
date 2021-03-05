from socket import *


BUFFERSIZE = 1024
soc = socket(AF_INET, SOCK_DGRAM)
soc.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
soc.bind(('',9999))
while True:
	data, addr = soc.recvfrom(BUFFERSIZE)
	data = data.decode()
	if not data:
		break
	print(data)
soc.close()














