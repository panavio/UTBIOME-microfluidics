## Very Rough Idea:
```
Camera (RPI)
   ↓
Image capture script
   ↓
Send image (HTTP)
   ↓
Backend server (YOLO runs inference)
   ↓
Prediction (bounding boxes / labels)
   ↓
Send results back
   ↓
Some action (log / alert / display on a dashboard?)
```

## RPI Send Data using HTTP
```
import requests
url = "http://SERVER_IP:8000/predict"

files = {"file": open("image.jpg", "rb")}
response = requests.post(url, files=files)

print(response.json())
```

## CV (Backend Using FastAPI)
```
from fastapi import FastAPI, File, UploadFile
from ultralytics import YOLO
import shutil

app = FastAPI()
model = YOLO("model.pt")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    with open("temp.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
```

    results = model("temp.jpg")

    return {"result": str(results)}
