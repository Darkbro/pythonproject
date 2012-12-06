#!/usr/bin/python
from socket import *
from time import ctime

HOST = ''
PORT = 20122
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpSerSock = socket(AF_INET, SOCK_DGRAM)
udpSerSock.bind(ADDR)

while True:
	print 'wauting for connecting...'
	data, addr = udpSerSock.recvfrom(BUFSIZ)
	udpSerSock.sendto('[%s] %s' % (ctime(), data), addr)
	print 'reciveed from :', addr
udpSerSock.close()
