import numpy
from ultralytics import YOLO

model = YOLO("yolov8n.pt", "v8")


detection_output= model.predict(source="probeimages/intersection.jpg", conf=0.25, save=True)
print(detection_output)

print(detection_output[0].numpy())