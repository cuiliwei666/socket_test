from socket import * 
import sys

soc = socket(AF_INET, SOCK_DGRAM)

BUFFERSIZE = 1024
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST, PORT)

while True:
	in_data = input('请输入您的消息')
	soc.sendto(in_data.encode(), ADDR)
	data, addr = soc.recvfrom(BUFFERSIZE)
	print(data.decode())


















