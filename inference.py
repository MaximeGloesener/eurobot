from ultralytics import YOLO
import os 

# load le meilleur modèle
model = YOLO('yolov8n.pt')



for img in os.listdir('datasets/robot/images'):
    results = model('datasets/robot/images/'+img)
