from PIL import Image,ImageDraw,ImageFont


"""
第 0000 题： 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
"""

def add_num(img,num_text,num_size):

    #获取一个Image可以直接操作的对象
    img = Image.open(img) 
    draw = ImageDraw.Draw(img)

    #设置字体文件，大小，颜色
    font = ImageFont.truetype("consolab.ttf",size=num_size)
    fillcolor = "#ff0000"
    width,height = img.size
    
    #绘制
    draw.text( (width - 40,10),num_text,font=font,fill=fillcolor)
    
    #保存结果
    img.save("num.png","png")

if __name__ == "__main__":
    img = "1.png"
    add_num(img,"99",30)