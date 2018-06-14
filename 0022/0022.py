""" 
iPhone 6、iPhone 6 Plus 早已上市开卖。请查看你写得 第 0005 题的代码是否可以复用。
"""

import os
from PIL import Image


def resize(img_dir, MAX_RESIZE, out_dir):
    try:
        for file in os.listdir(img_dir):

            #读取文件
            img_file = os.path.join(img_dir, file)
            img = Image.open(img_file)

            #调整大小
            out = img.resize(MAX_RESIZE)

            #如果out文件夹不存在则新建一个
            if not os.path.exists(out_dir):
                os.mkdir(out_dir)

            #保存结果
            out_img = os.path.join(out_dir, file)
            out.save(out_img)

    except Exception as e:
        print("操作失败！", e)


if __name__ == '__main__':
    img_dir = 'img'
    out_dir = 'out'
    MAX_RESIZE = (750, 1334)
    resize(img_dir, MAX_RESIZE, out_dir)
