import socket, SocketServer, urllib, htmllib

bufsize = 8192

class TCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		client_address = self.client_address
		#while True:
		client_data = self.request.recv(bufsize)
                header = get_header(client_data)
                print 'Got ' + header[1] + ' from ' + str(client_address)
                print 'Now trying to fetch the desired website.'
                website = get_website(header[1])
        	self.request.send(website)

def get_header(request):
        while True:
                line_end = request.find('\n')
                if line_end != -1:
                        break
        print '%s' % request[:line_end] #debug
        data = request[:line_end+1].split()
        return data

def get_website(url):
        try:
                urlhandler = urllib.urlopen(url)
                html = urlhandler.read()
        except IOError:
                print 'Can\'t establish a connection to: ' + url
                html = 'IOError'
        except:
                print 'Some other exception occurred.'
                html = 'Other exception'
        return html

def annoying(html_input):
        
        return annoying_output

def start_server(host='127.0.0.1', port=8080, timeout=10,
                 handler=TCPHandler, mode='n'):
        tcp_server = SocketServer.TCPServer((host, port), handler)
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
