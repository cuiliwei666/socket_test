from socket import *

HOST = '192.168.43.255'
PORT = 9999
ADDR = (HOST, PORT)

soc = socket(AF_INET, SOCK_DGRAM)
soc.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

while True:
	in_data = input('请输入要群发的消息：')
	soc.sendto(in_data.encode(), ADDR)
	if not in_data:
		break
soc.close()




















