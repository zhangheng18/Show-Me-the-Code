"""
纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
"""

import xlrd
from lxml import etree


#读取xls
def read_xls(xlsname, sheetname):
    xls = xlrd.open_workbook(xlsname)
    sheet = xls.sheet_by_name(sheetname)
    data = {}
    for n in range(sheet.nrows):
        row_d = sheet.row_values(n)
        data[row_d[0]] = row_d[1]

    return data


#写入到xml
def write_xml(xmlname, data, comment):
    #建立root根节点
    root = etree.Element('root')

    #添加注释
    comm = etree.Comment(comment)
    root.append(comm)

    #添加一个子节点city
    child = etree.SubElement(root, xmlname)
    #添加文字
    child.text = str(data)

    #生成xml树对象
    tree = etree.ElementTree(root)

    #写入到表格
    tree.write(
        xmlname + '.xml',
        pretty_print=True,
        xml_declaration=True,
        encoding='utf-8')


if __name__ == "__main__":
    comment = '城市信息'
    data = read_xls('city.xls', 'city')
    write_xml('city', data, comment)
