import socket

buffsize = 4096
client_data = raw_input('Enter sting to echo: ')

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', 0))
server_address = ('127.0.0.1', 33333)
s.sendto(client_data, server_address)
server_data, server_address = s.recvfrom(buffsize)
print 'Got: ' + server_data + ' from ' + str(server_address)
s.close()



