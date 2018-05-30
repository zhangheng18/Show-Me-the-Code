"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

import re
from collections import Counter
with open("test.txt","r") as f:
    text = f.read().lower()
text = re.sub(r'[,.!?:"]',' ',text)
text = re.sub(r'-','',text)

#统计词频
counts = Counter(text.split())
#按顺序输出结果
print(counts.most_common())