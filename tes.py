import socket, SocketServer, urllib, htmllib

bufsize = 8192

class TCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		self.timeout = 20
		self.client_data = self.request.recv(bufsize)
                self.method, self.url, self.protocol = self.get_header(self.client_data)
                print 'Got ' + self.method + ' ' + self.url + ' ' + self.protocol +' from ' + str(self.client_address)
                print 'Now trying to fetch the desired website.'
                # Further processing depends on the method
                if self.method == 'CONNECT':
                        print 'CONNECT method.'
                        self.connect_method()
                elif self.method in ('OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE'):
                        print 'Other method.'
                        self.other_methods()
                
                        
                
 #               website = self.get_website()
#        	self.request.send(website)
        	print 'Success.'

        def connect_method(self):
                pass

        def other_methods(self):
                self.path = self.url[7:]
                index = self.path.find('/')
                host = self.path[:index]
                self.path = self.path[index:]
                print 'Connecting to: ' + host, self.path
                self._establish_connection(host)
                print 'Connected.'
                print 'Sending: ' + self.method, self.path, self.protocol
                self.target.send('%s %s %s\n'%(self.method, self.path, self.protocol) + self.client_data)
                print 'Sent.'
                self.client_data = ''
                self._read_write()

        def _read_write(self):
                time_out_max = self.timeout/3
                sockets = [self.client, self.target]
                count = 0
                while True:
                        count += 1
                        (recv, _, error) = select.select(sockets, [], sockets, 3)
                        if error:
                                break
                        if recv:
                                for in_ in recv:
                                        data = in_.recv(bufsize)
                                        if in_ is self.client:
                                                out = self.target
                                        else:
                                                out = self.client
                                        if data:
                                                out.send(data)
                                                count = 0
                        if count == time_out_max:
                                break

        def _establish_connection(self, host):
                index = host.find(':')
                if index != -1:
                        port = int(host[index+1:])
                        host = host[:index]
                else:
                        port = 80
                socket_family, _, _, _, address = socket.getaddrinfo(host, port)[0]
                self.target = socket.socket(socket_family)
                return self.target.connect(address)

        def get_header(self, request):
                while True:
                        line_end = request.find('\n')
                        if line_end != -1:
                                break
                data = request[:line_end+1].split() # split the header into method, path and protocol
                return data

        def get_website(self):
                try:
                        urlhandler = urllib.urlopen(self.url)
                        html = urlhandler.read()
                except IOError:
                        print 'Can\'t establish a connection to: ' + self.url
                        html = 'IOError'
                except:
                        print 'Some other exception occurred.'
                        html = 'Other exception'
                return html

        def annoying(html_input):
                pass        

def start_server(host='127.0.0.1', port=8080, timeout=10,
                 handler=TCPHandler, mode='n'):
        tcp_server = SocketServer.ThreadingTCPServer((host, port), handler)
        print 'Proxy is available at %s:%d' %(host, port)
        tcp_server.serve_forever()
                        

if __name__ == '__main__':
        start_server()
#        import sys
#        try:
#                start_server(mode=sys.argv[1])
#        except KeyboardInterrupt:
#                print 'Keyboard Interrupt'
#        except:
#                print 'Usage: proxy [a|n] - annoying | normal'
