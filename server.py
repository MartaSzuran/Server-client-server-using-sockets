# server

import socket
import sys

# To create the server we need to create a socket object, listen for incoming connections, accept clients
# when client try to connect and send and receive data.
# Once we create a socket object we you can use functions to operate with it.

# test if socket object has been created successfully
try:
    socket_stream = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket object successfully created.")
except socket.error as err:
    print("Socket creation failed.")

# create variable for port
port = 1024

# test getting host_ip
try:
    host_name = socket.gethostname()
except socket.gaierror:
    print("There was an error resolving the host.")
    sys.exit()

# bind() assigns the address specified by local address to the socket
# test if address is assigns successfully
try:
    socket_stream.bind((host_name, port))
except socket.error as err:
    print("Error occurs while assigning a local address using bind().")

# listen() for connections on a socket
# test listen
try:
    socket_stream.listen(5)
except socket.error as err:
    print("Error occurs while listen() method.")

while True:
    # return the address of our port
    # test if connection has been established
    try:
        connection, address = socket_stream.accept()
        print("Connection establish to address:", address)
    except socket.error as err:
        print("Connection to the", address, "cannot be establish.")

    # create a massage variable and send it to the client using send() function
    massage_var = "Thank you for connecting."
    encode_massage_var = massage_var.encode("ascii")
    connection.send(encode_massage_var)
    # another way - clt.send(bytes("network programming using python", "utf-8"))

    # create variable for data received from client server using recv() function
    # parameter is an amount of bytes
    while True:
        data = connection.recv(1000)
        if data:
            # need to use decode() function to don't have b"...." output
            print(data.decode())
        else:
            print("The connection has been finished.")
            connection.close()
            break
