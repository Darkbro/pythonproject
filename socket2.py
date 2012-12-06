#!/usr/bin/python
from socket import *

#HOST = '172.18.0.233'
HOST = ''
PORT = 20121
ADDR = (HOST, PORT)
BUFSIZ = 1024

tcpclisock = socket(AF_INET, SOCK_STREAM)
#tcpsersock.bind(ADDR)
#tcpsersock.listen(5)
tcpclisock.connect(ADDR)

while True:
#	data = tcpsersock.recv(BUFSIZ)
	data = raw_input('>')
	if not data:
		break
	tcpclisock.send(data)
	data = tcpclisock.recv(BUFSIZ)
	if not data:
		break
	print data
tcpclisock.close()


