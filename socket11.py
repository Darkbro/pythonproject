#!/usr/bin/python
from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 20126))
s.listen(10)

while True:
	conn, addr = s.accept()
try:
	conn.settimeout(5)
	buf = conn.recv(1024)
	if buf == '1':
		conn.send('welcome to server')
	else:
		conn.send('please go out')
except socket.timeout:
	print 'timeout'

conn.close()
