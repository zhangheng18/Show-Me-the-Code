"""
 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""



# 生成激活码的函数
import uuid
def Generate_Code(counts,length=20):
    key_list = []

    for i in range(counts):
        key = str(uuid.uuid4())[:length]
        if key not in key_list:
            key_list.append(key)

    return key_list

import pymysql


if __name__ == "__main__":
    
    key = Generate_Code(200,20)

    #创建数据库连接
    conn = pymysql.connect( 
        host = "127.0.0.1", 
        user = "root", 
        password = "", 
        database = "test", 
        charset = 'utf8',
        cursorclass=pymysql.cursors.DictCursor)
    
    try:
        #创建一个游标对象 cursor
        with conn.cursor() as cursor:
    
            #执行 SQL，如果code表存在则删除
            cursor.execute("DROP TABLE IF EXISTS code")
            
            #创建code数据表
            sql = """CREATE TABLE code(
                id INT UNSIGNED AUTO_INCREMENT,
                code VARCHAR(32) NOT NULL,
                PRIMARY KEY(id)
            )ENGINE=InnoDB DEFAULT CHARSET=utf8;
            """
            cursor.execute(sql)

            #批量插入数据
            cursor.executemany("INSERT INTO code(code) VALUES(%s);",key)
        #提交更改
        conn.commit()

        with conn.cursor() as cursor:
            #查询结果
            cursor.execute("SELECT * FROM code;")
            print( cursor.fetchall() )

    finally:
        conn.close()
