"""
 用 Python 写一个爬图片的程序，爬 这个链接里的日本妹子图片 :-)http://tieba.baidu.com/p/2166231880
"""

import os
import re
import requests
import threading


def save_img(url,filename):
    try:
        #content的内容即为图片的二进制
        img = requests.get(url,timeout=3).content       
        print('downing ..... {}'.format(filename) )

        #保存图片
        with open(filename,'wb') as f:
            f.write(img)
    except Exception as e:
        print(e)


def thread_get(urls,img_dir):
    
    if not os.path.exists(img_dir):os.mkdir(img_dir)

    l = []
    for url in urls:
        imgname = url.split('/')[-1]
        filename = os.path.join(img_dir,imgname)
        #绑定线程
        t = threading.Thread(target=save_img,args=(url,filename))
        l.append(t)

    #启动线程
    for i in l:
        i.start()

    #阻塞线程等待结束
    for i in l:
        i.join()

if __name__ == "__main__":
    img_dir = 'img'
    url = "http://tieba.baidu.com/p/2166231880"
    html = requests.get(url)
    
    #获取所有图片地址
    img_urls = re.findall(r'img pic_type="0" class="BDE_Image" src="(.*?)"',html.text)
    
    thread_get(img_urls,img_dir)