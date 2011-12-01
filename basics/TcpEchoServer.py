import socket

buffsize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 33333))

s.listen(1)
connection, client_address = s.accept()

while True:
	client_data = connection.recv(buffsize)
	if client_data.strip() == 'bye':
		break
	print 'Got ' + client_data + ' from ' + str(client_address)
	connection.send(client_data.upper())


