# Client Code
import socket

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())   # Ammend to actual server IP
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT' 
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) #pad with blanks spaces to make up 64 bytes
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send_msg('Hello World!')
send_msg('This is Socket Programming!')
input() # For testing multiple client connection only. Remove in production
send_msg(DISCONNECT_MESSAGE)