from socket import *
from multiprocessing import Process


client_list = []


class Conn_Process(Process):
	def __init__(self,conn):
		super().__init__()
		self.conn = conn


	def run(self):
		global client_list
		client_info = {}
		self.conn.send('请输入您的名字:'.encode())
		name_ = self.conn.recv(10).decode()
		client_info['name'] = name_
		client_info['ip'] = self.conn.getpeername()
		client_list.append(client_info)
		print(client_info)
		while True:
			data = self.conn.recv(1024)
			recv_data = data.decode()
			print(client_info['name'], ': ',recv_data)
			if not recv_data:
				break
			self.conn.send('i"m ok'.encode())
		self.conn.close()



def main():
	soc = socket(AF_INET,SOCK_STREAM)
	soc.bind(('127.0.0.1',9999))
	soc.listen(5)
	while True:
		conn, addr = soc.accept()
		print('receive from ',addr)
		p = Conn_Process(conn)
		p.start()
	soc.close()
	print(client_list)


if __name__ == '__main__':
	main()









