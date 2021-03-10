from socket import *
import sys,os

BUFFERSIZE = 1024


s = socket(AF_UNIX, SOCK_STREAM)
server_address = './test'
if os.path.exists(server_address):
	os.unlink(server_address)
s.bind(server_address)
s.listen()
while True:
	c, addr = s.accept()
	while True:
		data = c.recv(BUFFERSIZE)
		if not data:
			c.close()
			break
		print(data.decode())
		c.send('服务器已收到您的消息了！'.encode())
		






