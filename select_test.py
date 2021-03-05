from socket import *
from select import *

BUFFERSIZE = 1024

s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',9999))
s.listen(5)
'''
烟恋上了手指，手指却把香烟给了嘴唇，香烟亲吻着嘴唇，内心却给了肺。肺只知得到了香烟的真心，却不知伤害了自己。到底是手指的
背叛成就了烟的梦想，还是嘴唇的贪婪促成了肺的伤害。人生如烟，岁月无痕。烟自多情，却把自己烧的只剩下屁股。
'''
rlist = [s]
wlist = []
xlist = []
while True:
	rs, ws, xs = select(rlist, wlist, xlist)
	for r in rs:
		if r is s:
			conn, addr = s.accept()
			print('connect from ',addr)
			rlist.append(conn)
		else:
			data = r.recv(BUFFERSIZE)
			if not data:
				rlist.remove(r)
				print(r.getpeername(),'has disconnectd')
				r.close()
				break
			print(r.getpeername(),': ',data.decode())
			r.send('服务器收到了您发送的消息！'.encode())
	for w in ws:
		pass
	for x in xs:
		pass































