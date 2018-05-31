"""
你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""

import re
from collections import Counter
import os

def most_common(filename):
    #读取文件，并全部转化为小写排除干扰
    with open(filename,"r") as f:
        text = f.read().lower()
    
    #将标点等干扰全部替换成空格
    text = re.sub(r'[,.!?:"]',' ',text)
    text = re.sub(r'-','',text)

    #统计词频
    counts = Counter(text.split())
    
    #过滤常见高频词
    ignore_words=['a','at','an','and','as','by','be','of','said','for','i','it','after',"it's",'in','on','is','she','us','to','not','has','the','that','this','with','have']
    for word in ignore_words:
        if word in counts:
            counts[word] = 0

    #输出最重要的1个词
    print("{} the most word is {}".format(filename,counts.most_common(1)[0][0]) )


if __name__ == '__main__':
    dirary_dir = 'dirary'
    #遍历dirary目录的文件
    for file in os.listdir(dirary_dir):
        filename = os.path.join(dirary_dir,file)
        most_common(filename)