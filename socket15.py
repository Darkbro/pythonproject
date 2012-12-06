#!/usr/bin/python
import socket
import sys

HOST = sys.argv[1]
PORT = sys.argv[2]
filename = sys.argv[3]

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
	print 'Strange error creating socket:%s' % msg
	sys.exit(1)

try:
	port = int(PORT)
except ValueError:
	try:
		port = socket.getservbyname(PORT, 'tcp')
	except socket.error, msg:
		print 'Counld not find your port:%s' % msg
		sys.exit(1)

try:
	s.connect((HOST, PORT))
except socket.gaierror, msg:
	print 'Address-related error connecting to server:%s' % msg
	sys.exit(1)
except socket.error, msg:
	print 'Connecting Error:%s' % msg
	sys.exit(1)
try:
	s.sendall("GET %s HTTP/1.0\r\n\r\n" % filename)
except socket.error, msg:
	print 'Error sending data:%s' % msg
	sys.exit(1)
try:
	s.shutdown(1)
except socket.error, msg:
	print 'Error sending data:%s' % msg
	sys.exit(1)

while True:
	try:
		buf = s.recv(2048)
	except socket.error, msg:
		print 'Error reciving data:%s' % msg
		sys.exit(1)
	if not len(buf):
		break
	sys.stdout.write(buf)
