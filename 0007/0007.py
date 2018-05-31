"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import os

def count_lines(code_dir):
    code_lines = 0
    blank_lines = 0
    comment_lines = 0
    comment = False
    for file in os.listdir(code_dir):
        filename = os.path.join(code_dir,file)
        with open(filename,"r") as f:
            text = f.readlines()

        for line in text:
            #排除左边空格的干扰
            line = line.lstrip(' ')

            #单行注释
            if(line.startswith('#')):
                comment_lines += 1  
            
            #这里设置一个comment 作为开关
            elif(line.startswith("'''") or line.startswith('"""')):
                comment_lines += 1
                comment = not comment  
            
            #“”“内的换行也算作注释”“”
            elif(line.startswith('\n')):
                if comment:
                    comment_lines += 1
                else:
                    blank_lines += 1
            
            #非注释内的内容算作代码
            else:
                if comment:
                    comment_lines += 1
                else:
                    code_lines +=1

    total = code_lines + blank_lines + comment_lines
    print("共有代码:{}行".format(total))
    print("代码:{}行".format(code_lines))
    print("注释:{}行".format(comment_lines))
    print("空行:{}行".format(blank_lines))

if __name__ == '__main__':
    code_dir = 'code'
    count_lines(code_dir)