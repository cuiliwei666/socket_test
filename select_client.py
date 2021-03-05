from socket import *


BUFFERSIZE = 1024

s = socket()
s.connect(('127.0.0.1',9999))
while True:
	in_data = input('请输入您要发送的消息：')
	s.send(in_data.encode())
	if not in_data:
		break
	out_data = s.recv(BUFFERSIZE)
	print(out_data.decode())
s.close()











