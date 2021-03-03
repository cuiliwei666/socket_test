from socket import *
import sys

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

soc = socket(AF_INET,SOCK_DGRAM)
soc.bind(ADDR)

while True:
	data, addr = soc.recvfrom(BUFFERSIZE)
	print('receive from {}:{}'.format(addr, data.decode()))
	soc.sendto('服务器收到了你的消息'.encode(), addr)

	











