# Python Client Code
import socket

# Create a client socket (IPv4, TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (localhost on port 12345)
client_socket.connect(('localhost', 12345))

# Send data to the server
client_socket.send(b"Hello, Server!")

# Receive data from the server
data = client_socket.recv(1024)
print(f"Received from server: {data.decode()}")

# Close the connection
client_socket.close()
