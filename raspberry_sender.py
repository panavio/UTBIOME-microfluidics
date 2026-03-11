import socket
import struct
import os
import time

# Socket documentation https://docs.python.org/3/library/socket.html
# Struct documentation https://docs.python.org/3/library/struct.html 
# OS documentation https://docs.python.org/3/library/os.html
# For complete transparency, AI assisted in making this code (especially in understanding sockets and libraries used)

''' This code sends a byte array file to the computer, some vals need to be changed (specifically HOST)'''
# next steps could be automating the reconstructing images part because that code is not automated, this will make it so the entire process of taking an image which is stored in a folder is automatically sent to laptop!


HOST = "192.168.7.2" # This is a placeholder value needs to be the computers IP
PORT = 5001
WATCH_FOLDER = "File Sender" # Adjust this to whatever name we give the folder for automatic send on the Pi

sent_files = set()

def send_file(filepath):

    filename = os.path.basename(filepath)
    filesize = os.path.getsize(filepath)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        s.connect((HOST, PORT))

        s.sendall(struct.pack("!I", len(filename)))
        s.sendall(filename.encode())
        s.sendall(struct.pack("!Q", filesize))

        with open(filepath, "rb") as f:
            
            while True:
                data = f.read(4096)

                if not data:
                    break
            
                s.sendall(data)
    
    print("Sent:", filename)

os.makedirs(WATCH_FOLDER, exist_ok=True)

while True:
    files = os.listdir(WATCH_FOLDER)
    for file in files:
        
        path = os.path.join(WATCH_FOLDER, file)
        
        if path not in sent_files and os.path.isfile(path):
            send_file(path)
            sent_files.add(path)
    
    time.sleep(15) # so it isn't running constantly can change as needed
