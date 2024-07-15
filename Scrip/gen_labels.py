# #/home/yetian/Project/CrowdCounting-P2PNet/HeadHunter/crowdhuman284193,faa9000f2678b5e.jpg
# 123 129 186 193 0
# 214 97 272 171 0
# 318 109 376 177 0
# 486 119 547 193 0
# 559 105 612 162 0
# 596 40 668 123 0
# 731 139 800 222 0
# #/home/yetian/Project/CrowdCounting-P2PNet/HeadHunter/crowdhuman273275,cd061000af95f691.jpg
# 285 223 310 250 0
# 217 234 235 253 0
# 170 240 186 258 0
# 144 248 150 255 0
# 126 243 133 251 0
# 133 246 140 252 0
# -12 242 0 254 -1

import os
from PIL import Image


input_file = '/home/yetian/Project/Iter-Deformable-DETR/crowdhuman/CHuman_Valid.txt'
target_path = '/home/yetian/Project/Yolo_HeadDetection/Datasets/CrowdHumanHead/labels/val'  # 请替换为实际的目标路径
image_path = '/home/yetian/Project/Yolo_HeadDetection/Datasets/CrowdHumanHead/images/val'
# 打开输入文件并读取内容
with open(input_file, 'r') as file:
    lines = file.readlines()

# 初始化变量
current_image_path = None
current_targets = []


for line in lines:
    line = line.strip()
    if line.startswith('#'):

        if current_image_path and current_targets:

            filename = os.path.basename(current_image_path)
            print(filename)
            target_name = os.path.splitext(filename.replace('crowdhuman',''))[0] + '.txt'
            
            img_name = os.path.splitext(filename.replace('crowdhuman',''))[0] +'.jpg'
            img = Image.open(os.path.join(image_path,img_name))
            img_w,img_h = img.size
            
            target_file_path = os.path.join(target_path, target_name)
            
  
            with open(target_file_path, 'w') as target_file:
                for target in current_targets:
                    if target[-1] == 0:  # 检查是否有效
                        for i in range(4):
                            if target[i] < 0:
                                target[i] = 0
                  
                                
                        target[0] = target[0]/img_w
                        target[1] = target[1]/img_h
                        target[2] = target[2]/img_w
                        target[3] = target[3]/img_h
                        
                        x_center = (target[0] + target[2])/2
                        y_center = (target[1] + target[3])/2
                        w = target[2] - target[0]  #w
                        h = target[3] - target[1]  #h
                        
                        target_file.write(f"1 {x_center} {y_center} {w} {h}\n")
            
     
            current_image_path = None
            current_targets = []
        

        current_image_path = line[1:]  # 去掉开头的 '#'
    else:

        target = list(map(int, line.split()))
        current_targets.append(target)


if current_image_path and current_targets:
    filename = os.path.basename(current_image_path)
    target_name = os.path.splitext(filename)[0] + '.txt'
    target_file_path = os.path.join(target_path, target_name)
    
    with open(target_file_path, 'w') as target_file:
        for target in current_targets:
            if target[-1] == 0:  # 检查是否有效
                target_file.write(f"1, {target[0]}, {target[1]}, {target[2]}, {target[3]}\n")
