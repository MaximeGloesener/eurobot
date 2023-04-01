from ultralytics import YOLO
import os 

# load le meilleur modèle -> remplacer 'yolov8n.pt' par le nom du modèle
model = YOLO('runs/detect/train/weights/best.pt')


# ici on teste juste sur les images utilisées pour l'entrainement, en pratique, vous allez 
# récupérer le flux vidéo de la caméra (avec OpenCV) et faire la détection sur chaque image

for img in os.listdir('datasets/robot/images'):
    # save = True pour sauvegarder l'image avec les boites englobantes dans le dossier runs/detect/predict
    results = model('datasets/robot/images/'+img, save=False)
    for result in results:
        print(result.boxes.xyxy)   # box with xyxy format, (N, 4)
        print(result.boxes.xywh)   # box with xywh format, (N, 4)
        print(result.boxes.xyxyn)  # box with xyxy format but normalized, (N, 4)
        print(result.boxes.xywhn)  # box with xywh format but normalized, (N, 4)
        print(result.boxes.conf)   # confidence score, (N, 1)
        print(result.boxes.cls)    # cls, (N, 1)
    break

