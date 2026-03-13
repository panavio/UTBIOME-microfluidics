import socket
import struct
import os
import time
import shutil

# Socket documentation https://docs.python.org/3/library/socket.html
# Struct documentation https://docs.python.org/3/library/struct.html 
# OS documentation https://docs.python.org/3/library/os.html
# For complete transparency, AI assisted in making this code

HOST = "192.168.7.2" # This is a placeholder value needs to be the computers IP
PORT = 5001
WATCH_FOLDER = "File_Sender" # Adjust this to whatever name we give the folder for automatic send on the Pi
SENT_FOLDER = "Sent_Files"

os.makedirs(SENT_FOLDER, exist_ok=True)

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
    shutil.move(filepath, os.path.join(SENT_FOLDER, filename))

os.makedirs(WATCH_FOLDER, exist_ok=True)

while True:
    files = os.listdir(WATCH_FOLDER)
    for file in files:
        
        path = os.path.join(WATCH_FOLDER, file)
        
        if path not in sent_files and os.path.isfile(path):
            send_file(path)
            sent_files.add(path)
    
    time.sleep(15) # so it isn't running constantly can change as needed
