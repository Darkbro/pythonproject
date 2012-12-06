#!/usr/bin/python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print 'Looking for port to use'

port = socket.getservbyname('http', 'tcp')
print 'Done'
print "%d" % port
s.connect(('www.baidu.com', port))
print 'Done'
