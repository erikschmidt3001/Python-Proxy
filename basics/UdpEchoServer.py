import socket

buffsize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 33333))

while True:
    client_data, client_address = s.recvfrom(buffsize)
    print 'Got: ' + client_data + ' from ' + str(client_address)
    s.sendto(client_data.upper(), client_address)
