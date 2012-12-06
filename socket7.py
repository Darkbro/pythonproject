#/usr/bin/python
import SocketServer

class hwRequestHandler(SocketServer.StreamRequestHandler):
	def handle(self):
		self.wfile.write("Hello World\r\n")

server = SocketServer.TCPServer(("", 2525), hwRequestHandler)
server.server_forever()
