#!/usr/bin/python
import socket
import select

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock1.connect(('192.168.1.1', 25))
sock2.connect(('192.168.1.1', 25))

while 1:
	rlist, wlist, elist = select.select([sock1, sock2], [], [], 5)
	
	if [rlist, elist, elist] == [ [], [], [] ]:
		print "Five seconds elapsed\n"
	else:
		for sock in rlist:
			print sock.recv(100)

