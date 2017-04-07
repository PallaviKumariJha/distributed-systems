# Author: Pallavi
# Created on: 17-01-2017
# Modified on: 

# The program handles request for a specified file from client

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
port = 4446
server_address = ('127.0.0.1', port)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    connection, client_address = sock.accept()

    # Receive the request and retransmit it
    try:
        data = connection.recv(1024)
        print ("server received request for", repr(data))
        filename = data.split()[1]
        filename = filename[1:]
        print filename
        f = open(filename,'rb')
        l = f.read()
        print l
        connection.send('\nHTTP/1.1 200 OK\n\n')
        connection.send(l)
        print('Done sending')
        connection.close()
    except:
        connection.send('\nHTTP/1.1 404 OK\n\n')
        connection.close()
    # Clean up the connection
    