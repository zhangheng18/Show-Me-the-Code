"""
 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""


with open('filtered_words.txt','r') as f:
        #读取内容到一个列表，并过滤每项中的'\n'
        text = ''.join(f.readlines()).strip('\n').split()

while True:
        #读取输入
        line = input("> ")
        #判断输入内容是否含有敏感词
        if any( [words in line for words in text]):
                print('Freedom')
        else:
                print('Human Rights')
     


