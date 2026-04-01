# this file is for computer 

import cv2
import socket
import YOLO
import ultralytics


model = YOLO("model.pt") # name of model

# Need to open RTSP stream from Pi
sock = socket.socket()
sock.connect("192.168.1.20", 5000)#((IP of Rpi, port number))


cap = cv2.VideoCapture("rtsp://192.168.1.20/stream") #(IP of Pi/stream))
    
while True:
    ret, frame = cap.read()
    if not ret: # just means if the frame wasn't sucessfully read
        break

    #resize image? cv2.resize(frame, (width, height))

    # run detection here
    results = model(frame)
    detected_objects = []
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0]) # for different classes RBC/WBC etc.
            name = model.names[cls]
            detected_objects.append(name)
    print(detected_objects)

    if len(detected_objects) > 0:
        message = ",".join(detected_objects)
    else:
        message = "none"
    sock.send(message.encode()) #put results here

    #show video
    annotated_frame = results[0].plot()
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) == 27: # this continue to play images every 1ms refresh and stops if ESC key is pressed
        break

cap.release()
sock.close()
cv2.destroyAllWindows()

