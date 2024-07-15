# Head-Detection-Yolov8
This repo provides a YOLOv8 model, finely trained for detecting human heads in complex crowd scenes, with the CrowdHuman dataset serving as training data. To boost accessibility and compatibility, I've reconstructed the labels in the CrowdHuman dataset, refining its annotations to perfectly match the YOLO format. 


# CrowdDataset Dataset&Yolo Format
Download the CrowdDataset from [https://www.crowdhuman.org/download.html]. I have provided the YOLO format labels in the `CrowdHumanHead/labels.zip` file. Simply unzip this file and place the contents in the `CrowdHumanHead/labels` directory.

# Some Useful Scrip as References
`Scrip/create_chuman.py` -- Creat txt format labels from ODGT.
`Scrip/gen_labels.py` -- Generate YOLO labels from txt format.
`Scrip/vis_labels.py`-- Visualize YOLO labels for label checking.