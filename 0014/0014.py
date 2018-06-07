"""
纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：
{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
请将上述内容写到 student.xls
"""

import pandas as pd

#按json格式读取内容，转化成pandas可以处理的DataFrame格式
df = pd.read_json('student.txt',orient='index')
#输出到student表格,表名student，忽略表头  print(df)
df.to_excel('student.xls',sheet_name='student',header=None)