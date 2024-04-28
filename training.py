from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data="C:/Users/VANSH KHANEJA/PROJECTS/OBJECT DETECTION/CUSTOM DATA/RBC COUNT/BCCD_Dataset-master/BCCD/data.yaml",
   epochs=10,
   batch=8,
   name='RBC_count_model'
)
