from ultralytics import YOLO
import os 

# load le meilleur modèle -> remplacer 'yolov8n.pt' par le nom du modèle
model = YOLO('yolov8n.pt')



for img in os.listdir('datasets/robot/images'):
    results = model('datasets/robot/images/'+img)
