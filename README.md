# Head-Detection-Yolov8
This repo provides a YOLOv8 model, finely trained for detecting human heads in complex crowd scenes, with the CrowdHuman dataset serving as training data. To boost accessibility and compatibility, I've reconstructed the labels in the CrowdHuman dataset, removing useless annotations, refining its annotations to perfectly match the YOLO format. 

# Detection Example
![273271,1b9330008da38cd6.jpg](ImageDetExample/273271,1b9330008da38cd6.jpg)

![273271,1bb16000e7a389a3.jpg](ImageDetExample/273271,1bb16000e7a389a3.jpg)

![273271,1bd660006ab0ac6a.jpg](ImageDetExample/273271,1bd660006ab0ac6a.jpg)

![273271,1be0200037d3046d.jpg](ImageDetExample/273271,1be0200037d3046d.jpg)

![273271,1c4c300008432bc2.jpg](ImageDetExample/273271,1c4c300008432bc2.jpg)

![273271,1c20c00070107528.jpg](ImageDetExample/273271,1c20c00070107528.jpg)

![273271,1c72c000a2ee47d5.jpg](ImageDetExample/273271,1c72c000a2ee47d5.jpg)

![273271,1cc7d000a31f3d60.jpg](ImageDetExample/273271,1cc7d000a31f3d60.jpg)

![273271,1ed81000290034fa.jpg](ImageDetExample/273271,1ed81000290034fa.jpg)

![273271,1f0ac00034c81048.jpg](ImageDetExample/273271,1f0ac00034c81048.jpg)

![273271,1f3ca000086fb919.jpg](ImageDetExample/273271,1f3ca000086fb919.jpg)


# CrowdDataset Dataset&Yolo Format
Download the CrowdDataset from [https://www.crowdhuman.org/download.html]. I have provided the YOLO format labels in the `CrowdHumanHead/labels.zip` file. Simply unzip this file and place the contents in the `CrowdHumanHead/labels` directory.


# Pre-trained YoloV8 Head Detection Model
Please download the model weight from this [Google Drive URL](https://drive.google.com/file/d/1qlBmiEU4GBV13fxPhLZqjhjBbREvs8-m/view?usp=sharing). 


# Model Inference 
`
python3 pred_yolo_v8.py
`


# Model Training 
`
python3 train_yolo_v8.py
`


# Some Useful Scrip as References
`Scrip/create_chuman.py` -- Creat txt format labels from ODGT.
`Scrip/gen_labels.py` -- Generate YOLO labels from txt format.
`Scrip/vis_labels.py`-- Visualize YOLO labels for label checking.

