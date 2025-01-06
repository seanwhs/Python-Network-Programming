import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT' 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket family, type

# Try binding the server to the address and handle any potential errors
try:
    server.bind(ADDR)
    print(f'[BIND SUCCESS] Server bound to {ADDR}')
except Exception as e:
    print(f'[BIND ERROR] Failed to bind server: {e}')
    exit()

def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f'{addr} : {msg}')
            conn.send('[MESSAGE RECEIVED] : message received'.encode(FORMAT))
    conn.close()

def start():
    server.listen()  # listen on socket
    print(f'[LISTENING] : Server is listening on {ADDR}')
    while True:
        conn, addr = server.accept()  # conn is a socket object
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.active_count() - 1}')  # subtract thread that runs always

print('[STARTING] server is starting...')
start()
