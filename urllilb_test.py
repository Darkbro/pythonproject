#!/usr/bin/python
import urllib
sock = urllib.urlopen('http://user.qzone.qq.com/451248559/infocenter/')
htmlSource = sock.read()
sock.close()
print htmlSource
