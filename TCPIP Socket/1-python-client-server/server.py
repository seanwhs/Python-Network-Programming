# Python Server Code
import socket

# Create a server socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific IP address and port
server_socket.bind(('localhost', 12345))

# Listen for incoming connections (max 1 client)
server_socket.listen(1)
print("Server is listening on port 12345...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connection established with {client_address}")

# Receive data from the client
data = client_socket.recv(1024)
print(f"Received data: {data.decode()}")

# Send a response back to the client
client_socket.send(b"Hello from the server!")

# Close the connection
client_socket.close()