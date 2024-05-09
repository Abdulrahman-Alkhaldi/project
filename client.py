# -----------------------------------------------------------
# a client that connects to a server and send a message,
# then wait to receive a message from the server
# Usage: python3 server.python
# the port and server IP address are hardcoded
# 2023 Dr. Fatma Alali
# -----------------------------------------------------------


import socket
import sys
import ssl

BUF_SIZE = 4096*1000
HOST = "localhost"
PORT = 9999

# TLS docs: https://docs.python.org/3/library/ssl.html#client-side-operation
def tls_connection(client, msg):
    
    context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH, cafile="cert.crt")
    # context.load_cert_chain(certfile="cert.crt", keyfile="key.pem")

    # Wrap the socket to secure it
    conn = context.wrap_socket(client, server_hostname=HOST)
    conn.connect((HOST, PORT))
    
    # Send a message
    conn.sendall(msg.encode())
    print("Message was sent")

    # Receive response
    data = conn.recv(BUF_SIZE)
    print("Client received:", data.decode())

    conn.close()

def regular_connection( client, msg):
    #connect to server
    client.connect((HOST, PORT))
    #send message
    client.sendall(msg.encode())
    print("Message was sent")

    #receive dat from server
    data = client.recv(BUF_SIZE)
    print("Client received", data.decode())
    client.close()

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # read data from user
    msg = input("Enter your message: ")
    #connect to server
    regular_connection(client, msg)
    # tls_connection(client, msg)
except Exception as e:
    print(f"An error occurred: {e}")