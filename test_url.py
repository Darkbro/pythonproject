import urllib, url_lister
usock = urllib.urlopen('http://www.baidu.com/')
parser = url_lister.URLList()
parser.feed(usock.read())
usock.close()
parser.close()
for url in parser.urls: 
	print url
