from ultralytics import YOLO

# Load a model
model = YOLO("yolov8x.yaml")  # build a new model from scratch
model = YOLO("yolov8x.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="./Datasets/CrowdHumanHead/CrowdHumanHead.yaml", 
            epochs=200,batch=24,device=[0,1,2,3,4,5],imgsz=800)
            #loggers='tensorboard')  # train the model
            #imgsz=640+160=800
metrics = model.val()  # evaluate model performance on the validation set
path = model.export(format="Pytorch")  # export the model to ONNX format
print("Export Path:",path)