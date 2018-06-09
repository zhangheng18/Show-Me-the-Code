"""
纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
	[1, 82, 65535], 
	[20, 90, 13],
	[26, 809, 1024]
]
"""

import json
import xlwt


def read(filename):
    with open(filename, 'r') as f:
        data = f.read()
    #格式化成json数据便于操作
    return json.loads(data)


def write(filename, data):
    #新建一个xls表格
    workbook = xlwt.Workbook()
    #新建表：numbers
    sheet_name = workbook.add_sheet('numbers')
    row = 0  #行

    #data 的内容[[1, 82, 65535], [20, 90, 13], [26, 809, 1024]]
    #遍历，写入到表
    for row_d in data:
        col = 0  #列
        for col_d in row_d:
            sheet_name.write(row, col, col_d)
            col += 1
        row += 1
    #保存成numbers.xls表
    workbook.save(filename)


if __name__ == '__main__':
    data = read('numbers.txt')
    write('numbers.xls', data)

# #借助pandas我们更简单的实现
# import pandas as pd
# df =pd.read_json('numbers.txt')
# df.to_excel('numbers.xls',header=None,index=False)