#!/usr/bin/python
import socket
import sys

HOST = ''
PORT = 20125
ADDR = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket Created'

try:
	s.bind(ADDR)
except socket.error, msg:
	print 'Bind Failed. Error Code : ' + str(msg[0]) + 'Message' + msg[1]
	sys.exit()
print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

while 1:

	conn, addr = s.accept()
	print 'Connected with' + addr[0] + ':' + str(addr[1])

	data = conn.recv(1024)
	reply = 'OK...' + data
	if not data:
		break
	conn.sendall(reply)
conn.close()
s.close()
