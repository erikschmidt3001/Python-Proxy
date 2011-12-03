import socket, SocketServer, urllib, htmllib

bufsize = 8192

class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        client_address = self.client_address
        client_data = self.request.recv(bufsize)
        method, url, protocol = get_header(client_data)
        print 'Got ' + url + ' from ' + str(client_address)
        print 'Now trying to fetch the desired website.'
        website = get_website(url)
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
                html = urlhandler.readlines()
                for lines in html:
                    output.feed(html[lines])
                html = output
        except IOError:
                print 'Can\'t establish a connection to: ' + url
                html = 'IOError'
        except:
                print 'Some other exception occurred.'
                html = 'Other exception'
        return html

def annoying(html_input):
        pass

def start_server(host='127.0.0.1', port=8080, timeout=10,
                 handler=TCPHandler, mode='n'):
    if mode == 'a':
        tcp_server = SocketServer.ThreadingTCPServer((host, port), handler)
    else:
        tcp_server = SocketServer.ThreadingTCPServer((host, port), handler)
    print 'Proxy is available at %s:%d' %(host, port)
    tcp_server.serve_forever()
                        

if __name__ == '__main__':
        start_server()
# import sys
# try:
# start_server(mode=sys.argv[1])
# except KeyboardInterrupt:
# print 'Keyboard Interrupt'
# except:
# print 'Usage: proxy [a|n] - annoying | normal'


