#!/usr/bin/python
from SocketServer import (TCPServer as TCP, StreamRequestHandler as SRH)
from time import ctime

HOST = ''
PORT = 20123
#BUFSIZ = 1024
ADDR = (HOST, PORT)

class MyRequestHandler(SRH):
	def handle(self):
		print 'connecting from ...',self.client_address
		self.wfile.write('[%s] %s' % (ctime(), self.rfile.readline()))
tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connecting...'
tcpServ.serve_forever()
