import socket

# Server

port = 12345

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketServer.bind(('', port))

print ("socket binded to %s" %(port)) 

socketServer.listen(5) #  means we can have 5 connections at once 6 one will be refused

while True:
    #establish connection with client
    socketObject, address = socketServer.accept() # because it returns a tuple
    
    socketObject.send("Thanks for connecting\n".encode())
    
    socketObject.close()
    
    