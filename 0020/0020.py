"""
 第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日通话详单.xls 文件。写代码，对每月通话时间做个统计。
"""
import re
import xlrd


#统计时长
def collect_times(xlsname):
    #读取第一个表格数据
    xls = xlrd.open_workbook(xlsname)
    sheet = xls.sheet_by_index(0)

    sum_time = 0
    caller_sum = 0

    #去掉表头
    for n in range(1, sheet.nrows):
        #读取通话时长与呼叫类型两列数据
        call_time, call_type = sheet.row_values(n)[3:5]
        #通过正则，得到时间，如9分23秒返回(9,23)
        Min, Sec = re.match(r'(\d*?)[分]?(\d+)秒', call_time).groups()

        #转化成秒
        if Min == '': Min = '0'
        times = int(Min) * 60 + int(Sec)

        #统计主叫时间
        if call_type == "主叫":
            caller_sum += times
        sum_time += times

    #打印统计结果
    print("本月主叫通话时间：%s分%s秒" % (divmod(caller_sum, 60)))
    print("本月被叫通话时间：%s分%s秒" % (divmod(sum_time - caller_sum, 60)))
    print("本月通话时间总计：%s分%s秒" % (divmod(sum_time, 60)))


if __name__ == "__main__":
    data = collect_times('2018年06月语音通信.xls')
