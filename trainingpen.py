from roboflow import Roboflow
rf = Roboflow(api_key="vrP4RpVNc9cZOD4WQaYh")
project = rf.workspace("public-ra7iu").project("traffic-light-kuylw")
dataset = project.version(2).download("yolov8")

