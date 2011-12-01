import SocketServer

buffsize = 4096

class TCPEchoHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		client_address = self.client_address
		while True:
			client_data = self.request.recv(buffsize)
			if client_data.strip() == 'bye':
				print 'I got your "bye"'
				break
			print 'Got ' + client_data + ' from ' + str(client_address)
			self.request.send(client_data.upper())
server_address = ('127.0.0.1', 33333)
tcp_echo_server = SocketServer.TCPServer(server_address, TCPEchoHandler)
tcp_echo_server.serve_forever()
