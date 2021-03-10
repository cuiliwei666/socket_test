from socket import *
import sys,os

s = socket(AF_UNIX, SOCK_STREAM)

server_address = './test'
BUFFERSIZE = 1024

s.connect(server_address)
while True:
	in_data = input('请输入您的消息：')
	s.send(in_data.encode())
	out_data = s.recv(BUFFERSIZE)
	print(out_data.decode())
	


















