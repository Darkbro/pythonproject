#!/usr/bin/python
from socket import *

print "Creating socket...."
s = socket(AF_INET, SOCK_STREAM)
print 'Done'
print 'Connecting to remote host...'
s.connect(('', 20127))
print 'Done'

