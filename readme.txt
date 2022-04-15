Server and client server.

Technology - python - library socket

The primary socket API functions and methods used are:

    socket() - creating object
    .bind() 
    .listen()
    .accept()
    .connect()
    .send()
    .recv()
    .close()

Server:
Create socket -> method bind() -> method listen() -> method accept() -> 
recv() and send() to client -> listen() 

Client server:

Create client socket -> method accept() -> send() and recv() -> close()

