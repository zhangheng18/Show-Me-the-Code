"""
将 第 0014 题中的 student.xls 文件中的内容写到 student.xml 文件中，如

下所示：
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!-- 
	学生信息表
	"id" : [名字, 数学, 语文, 英文]
-->
{
	"1" : ["张三", 150, 120, 100],
	"2" : ["李四", 90, 99, 95],
	"3" : ["王五", 60, 66, 68]
}
</students>
</root>
"""
import xml.dom.minidom as md
import xlrd


#读取xml内容到字典对象
def read_xls(filename, sheetname):
    #打开student.xls
    xls = xlrd.open_workbook(filename)
    #读取student表
    sheet = xls.sheet_by_name(sheetname)
    data = {}
    # 获取每行内容，以row为键，后面的列表为值，放到字典
    for n in range(sheet.nrows):
        row_d = sheet.row_values(n)
        data[row_d[0]] = list(row_d[1:])

    return data


#按照题目要求美化字符串
def pretty_str(dicts):
    text = "".join('{\n')
    for k in sorted(dicts.keys()):
        lists = dicts[k]
        s = '\t\t\t"%s" : ["%s", %d, %d, %d],\n' % (
            int(k), lists[0], int(lists[1]), int(lists[2]), int(lists[3]))
        text += s
    text += '\t\t}'
    text = text[::-1].replace(',', '', 1)[::-1]  #处理列表最后一项后面的，

    return text


#写入到xml
def write_xml(xmlname, data, comment):
    #新建xml文档对象
    xml = md.Document()
    #创建根节点
    root = xml.createElement('root')
    #创建student节点
    child = xml.createElement(xmlname)
    #先加入root节点
    xml.appendChild(root)
    #在root节点下加入student节点
    root.appendChild(child)

    #在student节点下添加注释
    comment = xml.createComment(comment)
    child.appendChild(comment)
    #在student节点下写入文字内容
    xmlcontent = xml.createTextNode(data)
    child.appendChild(xmlcontent)

    #美化后，保存到student.xml,"会被转义为＆quot，这里我们替换回来
    with open(xmlname + '.xml', 'w') as f:
        f.write(xml.toprettyxml().replace('&quot;', '"'))


if __name__ == "__main__":
    comment = '学生信息表 "id" : [名字, 数学, 语文, 英文]'
    data = read_xls('student.xls', 'student')
    data = pretty_str(data)
    write_xml('student', data, comment)
