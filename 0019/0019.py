"""
将 第 0016 题中的 numbers.xls 文件中的内容写到 numbers.xml 文件中，如下
所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<numbers>
<!-- 
	数字信息
-->

[
	[1, 82, 65535],
	[20, 90, 13],
	[26, 809, 1024]
]

</numbers>
</root>
"""

import pandas as pd
from lxml import etree


#读取xls,返回所需要样式的字符串
def read_xls(xlsname):
    df = pd.read_excel(xlsname, header=None)
    d = df.to_dict(orient='split')['data']
    return "\n\t[\n\t\t{},\n\t\t{},\n\t\t{}\n\t]\n\t".format(d[0], d[1], d[2])


#写入到xml
def write_xml(xmlname, data, comment):
    #建立root根节点
    root = etree.Element('root')

    #添加注释
    comm = etree.Comment(comment)
    root.append(comm)

    #添加一个子节点
    child = etree.SubElement(root, xmlname)
    #添加文字
    child.text = data

    #生成xml树对象
    tree = etree.ElementTree(root)

    #写入到表格
    tree.write(
        xmlname + '.xml',
        pretty_print=True,
        xml_declaration=True,
        encoding='utf-8')


if __name__ == "__main__":
    comment = '数字信息'
    data = read_xls('numbers.xls')
    write_xml('numbers', data, comment)
