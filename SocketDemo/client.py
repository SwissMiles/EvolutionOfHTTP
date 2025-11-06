import socket             

s = socket.socket()         

port = 12345                

s.connect(('127.0.0.1', port)) 

print (s.recv(1024).decode()) # number is how many bytes i can receive

s.close()     
     