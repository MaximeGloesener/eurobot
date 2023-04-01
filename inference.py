from ultralytics import YOLO
import os 

# load le meilleur modèle -> remplacer 'yolov8n.pt' par le nom du modèle
model = YOLO('runs/detect/train/weights/best.pt')


# ici on teste juste sur les images utilisées pour l'entrainement, en pratique, vous allez 
# récupérer le flux vidéo de la caméra (avec OpenCV) et faire la détection sur chaque image

for img in os.listdir('datasets/robot/images'):
    results = model('datasets/robot/images/'+img)
    break
