from ultralytics import YOLO

# Load the model.
model = YOLO('yolov8n.pt', "v8")

# Training.
results = model.train(
   data='/home/cristian/Desktop/LazarIA/Traffic-Light-2/data.yaml',
   name= 'yolov8n_lights',
   imgsz=640,
   epochs=25,
   batch=8,
   )