"""
一个HTML文件，找出里面的正文。
"""
from CxExtractor import CxExtractor
cx = CxExtractor()

#从读取内容
#html = cx.getHtml("https://github.com/Yixiaohan/show-me-the-code")
html = cx.readHtml("show-me-the-code.html",'utf-8')

#过滤干扰标签
content = cx.filter_tags(html)

print( cx.getText(content))