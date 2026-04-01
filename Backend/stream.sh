#!/bin/bash

# Start RTSP server
./mediamtx &

sleep 2

# Start camera stream
ffmpeg -f v4l2 -i /dev/video0 \
-vcodec libx264 \
-preset ultrafast \
-tune zerolatency \
-f rtsp rtsp://localhost:8554/stream

# some comments about ffmpeg lines:
# suing 8554 for RTSP 
# /dev/video0 is the name of camera on pi, not positive what its name will be,
# can find out by running "ls /dev/video*" on RPi I think

# Note: for bash need to run chmod +x stream.sh in terminal in the file directory where stored to make this executable
# then in terminal to run type ./stream.sh