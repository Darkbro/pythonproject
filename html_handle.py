#!/usr/bin/python
from sgmllib import SGMLParse
import htmlentitydefs

class BaseHTMLProcessor(SGMLParse):
	def reset(self):
		self.piece = []
		SGMLParse.reset(self)

	def unknown_starttag(self, tag, attrs):
		strattrs = ''.join([' %s='%s' ' % (key, value) for key, value in attrs])
		self.pieces.append('<%(tag)s%(strattrs)>' % locals())
	
	def unknown_endtag(self, tag):
		self.pieces.append('</(%tag)s>' % locals())

