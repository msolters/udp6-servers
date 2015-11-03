import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('fe80::204:25ff:fe19:1a3e', 10000)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
sock.listen(1)

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(16)
            print >>sys.stderr, 'received "%s"' % data
            if data:
                connection.sendall(data)
            else:
                break
    finally:
        connection.close()
