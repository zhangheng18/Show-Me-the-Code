"""
一个HTML文件，找出里面的链接。
"""

from urllib import request
import re

url = "https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432688314740a0aed473a39f47b09c8c7274c9ab6aee000"

req = request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')
#读取网页内容以utf-8解码
html = request.urlopen(req).read().decode('utf-8')

href = re.findall(r'href="(http.*?)"',html)
for link in href:
        print(link)




