import SocketServer, urllib

bufsize = 8192

class TCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        client_address = self.client_address
        client_data = self.request.recv(bufsize)
        method, url, protocol = get_header(client_data)
        website = get_website(url)
        self.request.send(''.join(website)) # Joining the list to a string

class AnnoyingTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        client_address = self.client_address
        client_data = self.request.recv(bufsize)
        method, url, protocol = get_header(client_data)
        #print 'I am ANNOYING'
        #print 'Got "' + method + ' ' + url + ' ' + protocol + '" from ' + str(client_address)
        website = get_website(url)
        website = annoy(website)
        self.request.send(''.join(website))

def get_header(request):
        while True:
                line_end = request.find('\n')
                if line_end != -1:
                        break
        data = request[:line_end+1].split()
        return data

def get_website(url):
    try:
        urlhandler = urllib.urlopen(url)
        data = urlhandler.readlines()
    except IOError:
        print 'Can\'t establish a connection to: ' + url
        data = 'IOError'
    except:
        print 'Some other exception occurred.'
        data = 'Other exception'
    return data

def annoy(data_input):
    output = change_title(data_input)
    output = change_links(output)
    output = change_images(output)
    return output

def change_title(data_input):
    output = []
    for data in data_input:    
        title_start = data.lower().find('<title>')
        if title_start != -1:
            text = data[:title_start+7] + 'Are you annoyed yet'
            title_end = data.lower().find('</title>')
            if title_end != -1:
                text += data[title_end:]
            output.append(text)
        else:
            output.append(str(data))
    return output

def change_images(data_input):
    output = []
    for data in data_input:
        img_start = data.lower().find('<img')
        if img_start != -1:
            text = data[:img_start+4] + ' src="http://python.org/images/python-logo.gif">'
            img_end = data.lower().find('</img>')
            if img_end != -1:
                text += data[img_end:]
            output.append(text)
        else:
            output.append(str(data))
    return output

def change_links(data_input):
    output = []
    for data in data_input:
        link_start = data.lower().find('<a')
        if link_start != -1:
            text = data[:link_start] + '<a href="http://www.hs.fi">Check this'
            link_end = data.lower().find('</a>')
            if link_end != -1:
                text += data[link_end:]
            output.append(text)
        else:
            output.append(str(data))
    return output

def start_server(host='127.0.0.1', port=8080, timeout=30,
                 handler=TCPHandler, mode='p'):
    if mode == 'a':
        handler = AnnoyingTCPHandler
        tcp_server = SocketServer.ThreadingTCPServer((host, port), handler)
        status = 'Annoying '
    else:
        status = 'Normal '
        tcp_server = SocketServer.ThreadingTCPServer((host, port), handler)
    print status + 'proxy is available at %s:%d' %(host, port)
    tcp_server.serve_forever()
                        

if __name__ == '__main__':
    import sys
    try:
        start_server(mode=sys.argv[1])
    except KeyboardInterrupt:
        print 'Keyboard Interrupt - Proxy stopped'
    except IOError:
        print 'Please wait for the socket to be available again.'
    except:
        print 'Usage: proxy [a|p] - annoying | normal'
