from socket import *

HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024




def main():
	s = socket()
	s.connect(ADDR)
	while True:
		input_data = input('请输入您的消息：')
		s.send(input_data.encode())
		data = s.recv(BUFFERSIZE)
		print(data.decode())
		if not input_data:
			break
	s.close()

if __name__ == '__main__':
	main()










