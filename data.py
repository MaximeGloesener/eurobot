# traitement des données et création des dossiers images et labels 
# étape 1 = dézipper les données dans le dossier eurobot => on a un dossier obj avec toutes les images et les labels 
# étape 2 = run le script qui se charge de créer les dossiers images et labels et de les remplir avec les images et les labels à partir du dossier obj
import os 

images_path = 'datasets/robot/images/'
labels_path = 'datasets/robot/labels/'
init_path = 'obj/'

# création des dossiers images et labels
if not os.path.exists(images_path):
    os.makedirs(images_path)
if not os.path.exists(labels_path):
    os.makedirs(labels_path)

# remplissage des dossiers images et labels à partir du dossier obj (contenant les images et les labels)
for img in os.listdir(init_path):
    if img.endswith('.jpg'):
        os.rename(init_path+img, images_path+img)
    if img.endswith('.txt'):
        os.rename(init_path+img, labels_path+img)

# suppression du dossier obj
os.rmdir(init_path)