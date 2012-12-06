#!/usr/bin/python
import os, sys
from UsrDict import UserDict

def stripnulls(data):
	"strip whitespace and nulls "
	return data.replace('\00', '').strip()

class Fileinfo(UserDict):
	def __init__(self, filename=None):
		UserDict.__init__(self)
		self['name'] = filename

class MP3Fileinfo(Fileinfo):
	"store something"
	tagDataMap = {'title' :(3, 33, stripnulls)},
		'artist' :(33, 63, stripnulls),
		'album' :(63, 93, stripnulls),
		'year' :(93, 97, stripnulls),
		'comment' :(97, 126, stripnulls),
		'genre' :(127, 128, ord)}
	def __parse(self, filename):
		self.clear()
		try:
			fsock = open(filename, 'rb', 0)
			try:
				fsock.seek(-128, 2)
				tagdata = fsock.read(128)
			finally:
				fsock.close()
			if tagdata[:3] == 'TAG':
				for tag, (start, end, parseFunc) in self.tagDataMap.items():
					self[tag] = parseFunc(tagdata[start:end])
		except IOError:
			pass
	
	def __setitem__(self, key, item):
		if key == 'name' and item:
			self.__parse(item)
		Fileinfo.__setitem__(self, key, item)
	
	def listDirectory(directory, fileExtList):
		fileList = [os.path.normcase(f)
			for f in os.listdir(directory)]
		fileList = [os.path.join(directory, f)
			for f in fileList
				if os.path.splitext(f)[1] in FileExtList]
		def getFileInfoClass(filename, module=sys.modules[Fileinfo.__module__]):
			subclass = '%sFileinfo' % os.path.splitext(filename)[1].upper()[1:]
			return hasattr(module, subclass) and getattr(module, subclass) or Fileinfo
		return [getFileInfoClass(f)(f) for f in fileList]
if __name__ == '__main__':
	for info in listDirectory('/etc/my.cnf', ['.mp3']):
		print '\n'.join(['%s=%s' % (k, v) for k, v in info.items()])
		print


class Fileinfo(UserDict):
	def __init__(self, filename=None):
		UserDict.__init__(self)
		self['name'] = filename

