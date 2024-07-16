from ultralytics import YOLO
import os

weight_path =r"./models/weights/best.pt"
# Load a model
model = YOLO(weight_path)  # load a pretrained model (recommended for training)
# 图片文件夹路径
image_folder = "./test_input_sample"

# 获取文件夹中所有图片文件的路径
image_paths = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('.jpg', '.png', '.jpeg'))]

# 遍历所有图片进行推理并保存结果
for image_path in image_paths:
    # results = model([image_path], device=[7])  # 使用指定的设备进行推理
    # for result in results:
        # boxes = result.boxes  # Boxes object for bounding box outputs
        # result.save(filename=f"result_{os.path.basename(image_path)}")  # 保存结果到磁盘
    results = model.predict(task="detect", source=image_path, imgsz=800, max_det=1000, conf=0.60, show_labels=False, show_conf=True, save=True, device="cpu", augment=True)