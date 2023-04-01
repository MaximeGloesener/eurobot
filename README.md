## Projet Eurobot

Objectif = aider l'équipe du robot pour la partie vision.

Entraînement de YOLO sur les images annotées pour détecter les palets de différentes couleurs. 

### Instructions
Utilisation de ultralytics pour entraîner YOLO: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)  
Exemple d'utilisation: [https://docs.ultralytics.com/usage/python/](https://docs.ultralytics.com/usage/python/)  
Custom dataset: [https://docs.ultralytics.com/yolov5/train_custom_data/](https://docs.ultralytics.com/yolov5/train_custom_data/)    

Pour utiliser facilement et reproduire les résultats:
1. Dézipper le dossier avec les images et labels dans le répertoire de travail.
2. Lancer le script data.py qui va gérer la création des dossiers pour l'entraînement en respectant la structure nécessaire. 
3. Si vous voulez entraîner le modèle, lancer le script train.py. Avant de lancer, vérifiez que vous avez choisi les bons paramètres si besoin.
4. A la fin de l'entraînement, les résultats sont stockés dans le dossier runs/detect/trainX avec X qui est le numéro de l'entraînement. Le meilleur modèle sera dans runs/detect/trainX/weights/best.pt. Lorsqu'on vous allez faire l'inférence, sélectionnez ce modèle. 
5. Inférer avec le fichier inference.py en choisissant les bons poids pour le modèle.  


## Que font les différents fichiers ? 

### dataset.yaml
Définition de la configuration pour les données. Mettre le path du dataset en respectant la structure datasets/nomjeudedonnées/images pour les images et datasets/nomjeudedonnées/labels pour les labels.   
Idéalement, avoir 80% des données pour l'entraînement et 20% pour la validation.

### data.py
Fichier qui permet de créer les dossiers avec les données en respectant le format demandé. 

### train.py
Fichier qui permet de lancer un entraînement.  
Voir [https://docs.ultralytics.com/modes/train/#arguments](https://docs.ultralytics.com/modes/train/#arguments) si vous voulez modifier d'autres paramètres pour l'entraînement.

### inference.py
Exemple d'inférence du modèle. Faites attention à bien choisir le bon modèle pour l'inférence. Si vous entraînez un modèle, vous devez définir le chemin vers celui-ci lors de l'inférence.   


### yolov8n.pt
Les poids du modèle pré-entrainé. Quand vous allez entraîner un modèle, vous allez avoir de nouveaux poids dans le dossier runs/detect/.  
Ici c'est le modèle le plus petit (nano) car vous allez run le modèle sur une raspberry pi. Vous pouvez tester d'autres modèles si vous voulez, la liste et les performances de chaque modèle pré-entrainé est disponile sur [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)

### Dossier runs
Dossier qui reprend les résultats des différents entraînements avec toutes les métriques et les poids du meilleur modèle obtenu lors de l'entraînement. 

