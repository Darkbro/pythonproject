#!/usr/bin/python
from  socket import *
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('', 20126))
time.sleep(2)
s.send('1')
print s.recv(1024)
s.close()
