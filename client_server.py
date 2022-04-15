# client server

import socket
import sys

# creating socket object for client
try:
    # TCP streaming = socket.SOCK_STREAM / UDP streaming = SOCK_DGRAM
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket object successfully created.")
except socket.error as err:
    print("Socket creation failed.")


# defining server name and port number
try:
    server_name = socket.gethostname()
except socket.gaierror:
    print("There was an error resolving the host.")
    sys.exit()

port_number = 1024

# use the connect() method to create a connection with the server
try:
    client_socket.connect((server_name, port_number))
except socket.error as err:
    print("There was problem with connection with server.")

# use the recv() method to receive data from server
# argument is how many bytes we want to receive
data = client_socket.recv(1000)
# print massage from server
print(data.decode("utf-8"))

name = (input("Write your name?\n"))
massage = "Hello, I am " + name

# send massage to the server
client_socket.send(massage.encode())

# close socket object
client_socket.close()
