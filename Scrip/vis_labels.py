import cv2

# 定义图像和标签文件的路径
image_path = "/home/yetian/Project/Yolo_HeadDetection/Datasets/CrowdHumanHead/images/train/273271,1a0d6000b9e1f5b7.jpg"
label_path = "/home/yetian/Project/Yolo_HeadDetection/Datasets/CrowdHumanHead/labels/train/273271,1a0d6000b9e1f5b7.txt"

# 读取图像
image = cv2.imread(image_path)
h,w,_ = image.shape

# 读取标签文件
with open(label_path, 'r') as file:
    lines = file.readlines()

# 解析标签文件并绘制边界框
for line in lines:
    parts = line.strip().split(' ')
    class_id = int(parts[0])
    x1, y1, x_w, y_h = map(float, parts[1:])
    
    # 绘制边界框
    cv2.circle(image, (int(x1*w), int(y1*h)), 5, (0, 0, 255), 2)
    x_c = int(x1*w)
    y_c = int(y1*h)
    x1 = x_c - int(x_w*w)//2
    y1 = y_c - int(y_h*h)//2
    x2 = x_c + int(x_w*w)//2
    y2 = y_c + int(y_h*h)//2
    
    
    cv2.rectangle(image,(x1, y1),(x2, y2), (0, 0, 255), 2)
    # cv2.putText(image, f'Class {class_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# 显示图像
cv2.imwrite('Example.jpg', image)

