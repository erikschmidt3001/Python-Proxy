import socket

buffsize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 33333)
s.connect(server_address)
print 'Server socket: ' + str(s.getpeername()) + ' | Client (own) socket: ' + str(s.getsockname())
while True:
	client_data = raw_input('Enter string to echo: ')
	s.send(client_data)
	if client_data.strip() == 'bye':
		break
	server_data = s.recv(buffsize)
	print 'Got: ' + server_data + ' from ' + str(server_address)
s.close()
