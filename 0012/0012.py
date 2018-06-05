"""
 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

from wfgfw import DFAFilter

#构造DFAFilter对象
f = DFAFilter()
#添加关键词
f.parse('filtered_words.txt')

while True:
        msg = input(">")
        #过滤消息，默认返回(布尔值，过滤过的内容)
        _,out = f.filter(msg)
        print(out)
