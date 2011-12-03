import socket, SocketServer

bufsize = 8192

class TCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		client_address = self.client_address
		while True:
			client_data = self.request.recv(bufsize)
                        header = get_header(self, client_data)
                        print 'Got ' + header[1] + ' from ' + str(client_address)
			self.request.send(header[1])

def get_header(self, request):
        while True:
                line_end = request.find('\n')
                if line_end != -1:
                        break
        print '%s' % request[:line_end] #debug
        data = request[:line_end+1].split()
        return data

def get_http(self, url):
        html = urlopen(url)
        return html

def start_server(host='127.0.0.1', port=8080, timeout=10,
                 handler=TCPHandler, mode='n'):
        tcp_server = SocketServer.ThreadingTCPServer((host, port), handler)
        print 'Proxy is available at %s:%d' %(host, port)
        tcp_server.serve_forever()
                        

if __name__ == '__main__':
        import sys
        
        start_server(mode=sys.argv[1])
