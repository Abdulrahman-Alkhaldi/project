# Python TLS Client-Server

This project contains a simple implementation of a TLS client-server in Python.

## Files

- [`client.py`](client.py): A client that connects to a server, sends a message, and waits to receive a message from the server.
- [`server.py`](server.py): The server that the client connects to.
- [`cert.crt`](cert.crt): The certificate file used for the TLS connection.
- [`key.pem`](key.pem): The private key file used for the TLS connection.

## Usage

1. Run the server:

```sh
python3 server.py
```
2. Run the client on a separate terminal and send a message:

```sh
python3 client.py
```

