#!/usr/bin/python
from socket import *
from time import ctime

HOST = ''
PORT = 20121
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpServer_Socket = socket(AF_INET, SOCK_STREAM)
tcpServer_Socket.bind(ADDR)
tcpServer_Socket.listen(5)

while True:
	print 'waiting for connecting...'
	tcpClient_Socket, addr = tcpServer_Socket.accept()
	print '...connecting from: ', addr
	
	while True:
		data = tcpClient_Socket.recv(BUFSIZ)
		if not data:
			break
		tcpClient_Socket.send('[%s] %s' % (ctime(), data))
		print [ctime()], ':', data
tcpClient_Socket.close()
tcpServer_Socket.close()

