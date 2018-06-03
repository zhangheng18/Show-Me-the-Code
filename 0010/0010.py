"""
使用 Python 生成类似于下图中的字母验证码图片。
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random
import string

# 随机字母:
def rndChar():
    return random.choice(string.ascii_letters)

# 随机背景色:
def bkgColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机字母色:
def charColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 容纳4个字符的宽度 240:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('consolab.ttf', 42)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=bkgColor())

# 输出文字:
letters = []
for t in range(4):
        char = rndChar()
        letters.append(char)
        draw.text((60 * t + random.randint(10,20), random.randint(10,20)),char, font=font, fill=charColor())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.png')

#显示
print(letters)
image.show()