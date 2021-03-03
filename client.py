from socket import *
client = socket(AF_INET, SOCK_STREAM)
client.connect(('127.0.0.1',9999))
recv_data = client.recv(1024)
print(recv_data.decode())
in_info = input()
client.send(in_info.encode())
while True:
	in_info = input('请输入您想发送的信息：')
	client.send(in_info.encode())
	if not in_info:
		break
	recv_data = client.recv(1024)
	print(recv_data.decode())
client.close()














