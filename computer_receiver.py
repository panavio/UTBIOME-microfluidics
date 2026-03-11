import socket
import struct
import os

# Socket documentation https://docs.python.org/3/library/socket.html
# Struct documentation https://docs.python.org/3/library/struct.html 
# OS documentation https://docs.python.org/3/library/os.html
# For complete transparency, AI assisted in making this code (especially for understanding libraries and how sockets work)

'''This code accepts a file from the Rasperry Pi and saves it to a folder, some values need to be changed, see comments.'''

HOST = "0.0.0.0"
PORT = 5001
SAVE_FOLDER = "Raspberry_Files" # Adjust this to whatever we want the name of the folder that stores the files to be called
os.makedirs(SAVE_FOLDER, exist_ok=True)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()

    print("Waiting for Raspberry Pi") 
    while True: 
        conn, addr = s.accept()

        with conn:
            print("Connected:", addr)

            # receive file length
            raw = conn.recv(4)
            name_len = struct.unpack("!I", raw)[0] # this converts bytes to int for length file name

            # receive filename
            filename = conn.recv(name_len).decode() # like scanf in C

            # receive file size
            raw = conn.recv(8)
            filesize = struct.unpack("!Q", raw)[0]
            filepath = os.path.join(SAVE_FOLDER, filename)

            print("Receiving:", filename)

            with open(filepath, "wb") as f:
                received = 0
            
                while received < filesize:
                    data = conn.recv(4096) # 4096 is size of memory pages, generally efficient
                    if not data:
                        break   

                    f.write(data)
                    received += len(data)
            
            print("Saved: ", filepath)

 
