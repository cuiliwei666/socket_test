from socket import *
import signal
import sys,os
from threading import Thread


HOST = '127.0.0.1'
PORT = 8888
ADDR = (HOST, PORT)
BUFFERSIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)


class ConnHandler(Thread):
	def __init__(self,c):
		super(ConnHandler,self).__init__()
		self.c = c
	def run(self):
		while True:
			data = self.c.recv(BUFFERSIZE)
			data = data.decode()
			print(data)
			self.c.send(r"i\'m ok".encode())
			if not data:
				break
		self.c.close()

def main():
	# signal.signal(SIGCHLD,SIG_IGN)
	s.bind(ADDR)
	s.listen(10)
	while True:
		print('到这了')
		c, addr = s.accept()
		print('connect from ',addr)
		p = ConnHandler(c)
		p.start()
		# c.close()











if __name__ == '__main__':
	main()








