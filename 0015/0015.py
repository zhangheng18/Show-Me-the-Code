"""
纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
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
    #添加一个city表
    sheet_name = workbook.add_sheet('city')
    row = 0  #行
    #data 的内容[('1', '上海'), ('2', '北京'), ('3', '成都')]
    for i, j in data.items():
        col = 0  #列
        sheet_name.write(row, col, i)
        sheet_name.write(row, col + 1, j)
        row += 1
    #保存成city.xls表
    workbook.save(filename)


if __name__ == '__main__':
    data = read('city.txt')
    write('city.xls', data)
