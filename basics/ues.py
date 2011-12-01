import SocketServer

class UDPEchoHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		client_address = self.client_address
		client_data, sock = self.request
		print 'Got : ' + client_data + ' from ' + str(client_address) 
		sock.sendto(client_data.upper(), client_address)

server_address = ('127.0.0.1', 33333)
udp_echo_server = SocketServer.UDPServer(server_address, UDPEchoHandler)

udp_echo_server.serve_forever()
