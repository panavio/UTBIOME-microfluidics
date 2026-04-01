# script for raspberry to receive results
# do we need this or is it ok if it just gives results on computer?
# Might be unnecessary

import socket

server = socket.socket()
server.bind(("0.0.0.0", 5000))
server.listen(1)

print("Waiting for computer connection...")
conn, addr = server.accept()
print("Connected from", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break

    message = data.decode()
    print("Detection:", message)

conn.close()