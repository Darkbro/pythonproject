#!/usr/bin/python
from xml.sax.handler import ContentHandler
from xml.sax import parse

class TestHandler(ContentHandler): 
#parse('website.xml', TestHandler())
	def __init__(self, inlist):
		self.inlist = inlist
	def startElement(self, name, attrs):
		print name, attrs.keys() 
if __name__ == '__main__':
	lt = []
	parse('website.xml', TestHandler(lt))
	print lt
