import socket

host = '127.0.0.1'
port = 10009
filename = "index.html"

socketObject = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketObject.connect((host, port))

# Send HTTP/0.9 GET request
socketObject.sendall(f"GET /{filename}\r\n".encode())

output_file = 'res_' + filename
with open(output_file, "w") as fo:
    while True:
        data = socketObject.recv(1024)
        if not data:
            break
        fo.write(data.decode())

socketObject.close()

print(f"Saved server response to {output_file}")
