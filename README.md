## Projet Eurobot

Objectif = aider l'équipe du robot pour la partie vision.

Entraînement de YOLO sur les images annotées pour détecter les palets de différentes couleurs. 

### Instructions
Utilisation de ultralytics pour entraîner YOLO: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)  
Exemple d'utilisation: [https://docs.ultralytics.com/usage/python/](https://docs.ultralytics.com/usage/python/)  
Custom dataset: [https://docs.ultralytics.com/yolov5/train_custom_data/](https://docs.ultralytics.com/yolov5/train_custom_data/)  


### dataset.yaml
Définition de la configuration pour les données. Mettre le path du dataset en respectant la structure datasets/nomjeudedonnées/images pour les images et datasets/nomjeudedonnées/labels pour les labels.   
Idéalement, avoir 80% des données pour l'entraînement et 20% pour la validation.


### train.py
Fichier qui permet de lancer un entraînement.  
Voir [https://docs.ultralytics.com/modes/train/#arguments](https://docs.ultralytics.com/modes/train/#arguments) si vous voulez modifier d'autres paramètres pour l'entraînement.

### inference.py
Exemple d'inférence du modèle.   


### yolov8n 
Les poids du modèle pré-entrainé. Quand vous allez entraîner un modèle, vous allez avoir de nouveaux poids dans le dossier runs/detect/.  
Ici c'est le modèle le plus petit (nano) car vous allez run le modèle sur une raspberry pi. Vous pouvez tester d'autres modèles si vous voulez, la liste et les performances de chaque modèle pré-entrainé est disponile sur [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

### Dossier runs
Dossier qui reprend les résultats des différents entraînements avec toutes les métriques et les poids du meilleur modèle obtenu lors de l'entraînement. 

