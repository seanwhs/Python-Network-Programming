# Server Code
import socket
from ssl import socket_error
import sys

# Function to create a socket
def create_socket():
    try:
        global host # globl variable for IP address
        global port # globl variable for TCP port
        global s    # globl variable for socket

        host = 'localhost'
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print(f'Socket creation error:: {str(msg)}')

# Function to Bind socket and listen for connections
def bind_socket():
        try:
            global host # access globl variable 
            global port # access globl variable for TCP port
            global s    # access globl variable for socket

            print(f'Binding port: {str(port)}')
            s.bind((host, port)) # host and port is passed in as a tuple
            s.listen(5)
        except socket.error as msg:
             print(f'Socket binding error: {str(msg)} \n"Retrying...."')
             bind_socket() # recurse

# Establish Connection with Client. Socket must be listening
def accept_socket():
    conn, address = s.accept() # accept() returns  connection object and a list containing IP:Port
    print(f'Connection Established. IP: {address[0]}, Port: {str(address[1])}')
    send_commands(conn)
    conn.close()

# Function to send commands to client
def send_commands(conn):
     while True:  #Infinite Loop
        cmd = input()
        if cmd.lower() == 'quit':
             conn.close()   # close connection
             s.close()      # close socket
             sys.exit()     # close command prompt
        if len(str.encode(cmd)) > 0:    # encode cmd str into bytes
             conn.send(str.encode(cmd))
             client_response = str(conn.recv(1024), 'utf-8') #buffer of 1024 Bytes
             print(client_response, end="")

def main():
     create_socket()
     bind_socket()
     accept_socket()

main(   )