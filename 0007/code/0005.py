"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

import os
from PIL import Image

MAX_RESIZE = (640,1130)

def resize(img_dir,MAX_RESIZE,out_dir):
    try:
        for file in os.listdir(img_dir):
            
            #读取文件
            img_file = os.path.join(img_dir,file)
            img = Image.open(img_file)
            
            #调整大小
            out = img.resize(MAX_RESIZE)
            
            #如果out文件夹不存在则新建一个
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)

            #保存结果
            out_img = os.path.join(out_dir,file)
            out.save(out_img)
            
    except Exception as e:
        print("操作失败！",e)

if __name__ == '__main__':
    img_dir =  'img'
    out_dir =  'out'
    resize(img_dir,MAX_RESIZE,out_dir)
