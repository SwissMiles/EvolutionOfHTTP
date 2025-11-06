import socket

port = 10009

socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socketServer.bind(('', port))
socketServer.listen(1)

print(f"HTTP/0.9 server running on port {port}...")

while True:
    socketObject, address = socketServer.accept()
    print(f"Connection from {address}")

    msg = socketObject.recv(1024).decode()
    if not msg:
        socketObject.close()
        continue

    msgParts = msg.split(" ", 1)
    if msgParts[0] == "GET":
        filename = msgParts[1].strip().lstrip("/").replace("\r", "").replace("\n", "")
        print(f"Requested file: {filename}")

        try:
            with open(filename, "r") as fo:
                data = fo.read()
                socketObject.sendall(data.encode())
                print(f"Sent contents of {filename} ({len(data)} bytes)")
        except IOError:
            print("File not found:", filename)

    socketObject.close()
