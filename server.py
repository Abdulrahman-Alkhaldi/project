# -----------------------------------------------------------
# Echo server: a server that accepts a connection, prints
# client message, then echo back (send) client message
# Usage: python3 server.python
# Seerver port is hardcoded to 9999
#
# 2023 Dr. Fatma Alali
# -----------------------------------------------------------

import socket
import ssl

BUF_SIZE = 4096*1000
PORT = 9999 
HOST = "localhost"

#TLS docs: https://docs.python.org/3/library/ssl.html#server-side-operation
def tls_connection(s):

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="cert.crt", keyfile="key.pem")

    client_socket, addr = s.accept()
    print("Client accepted:")

    # Wrap the client socket in an SSL layer
    secure_socket = context.wrap_socket(client_socket, server_side=True)

    # read and print the msg from the client
    data = secure_socket.recv(BUF_SIZE)
    print("Client sent:", data.decode())

    # Send back the same message to the client
    secure_socket.sendall(data)

def regular_connection(s):
    client, addr = s.accept()
    print("Client accepted")
    # read and print the msg from the client
    data = client.recv(BUF_SIZE)
    print("Client sent", data.decode())
    # send back the same message to the client
    client.sendall(data)


#create tcp socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
#listen to incomming connections
s.listen(1)
regular_connection(s)
# tls_connection(s)