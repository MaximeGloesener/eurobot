from ultralytics import YOLO



# Load a pretrained YOLO model (recommended for training)
model = YOLO('yolov8n.pt')

# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data='dataset.yaml', epochs=25)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model('datasets/robot/images/20221116_210157.jpg')



