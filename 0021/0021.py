"""
通常，登陆某个网站或者 APP，需要使用用户名和密码。密码是如何加密后存储起来的呢？请使用 Python 对密码加密。
"""

import os
import hashlib
import sqlite3
import binascii


#加密
def encrypt_passwd(passwd, salt=None):
    #把8位随机内容，转成16进制输出作为salt
    if salt is None:
        salt = binascii.b2a_hex(os.urandom(8))
    passwd = passwd.encode('utf-8')
    #用hashlib自带函数，sha256，迭代10000次，生成哈希值
    result = hashlib.pbkdf2_hmac('sha256', passwd, salt, 10000)

    #返回salt和密文
    return salt + binascii.b2a_hex(result)


#验证
def verify_passwd(salthash, passwd):
    if isinstance(salthash, str):
        salthash = salthash.encode('utf-8')

    #验证是否一致
    return encrypt_passwd(passwd, salt=salthash[:16]) == salthash


#初始化sqllite3数据库
def init_db():

    conn = sqlite3.connect("user.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS USER;")
    sql = """CREATE TABLE USER(
    ID INTEGER PRIMARY KEY autoincrement,
    USERNAME   TEXT NOT NULL,
    PASSWORD   TEXT NOT NULL);
    """
    c.execute(sql)
    conn.commit()
    return conn


#注册新用户
def register(conn, username, passwd):
    c = conn.cursor()
    #加密
    passwd = encrypt_passwd(passwd).decode('utf-8')

    #写入到数据库
    c.execute("INSERT INTO USER (ID,USERNAME,PASSWORD) VALUES (NULL,?,?)",
              (username, passwd))
    conn.commit()
    print("注册%s成功！" % (username))


#登录
def sgin(conn, username, passwd):
    c = conn.cursor()
    cur = c.execute("SELECT PASSWORD from USER where USERNAME=:name",
                    {"name": username})
    #获取密码
    pwd = cur.fetchone()
    #验证用户是否存在，并验证密码
    if pwd and verify_passwd(pwd[0], passwd):
        print('登录%s成功！' % (username))
        return True
    else:
        print("登录%s失败" % (username))
        return False


if __name__ == '__main__':
    c = init_db()
    register(c, "zhang3", "123456")
    register(c, "li4", "212")
    sgin(c, "zhang3", "1234")
    sgin(c, "li", "12")
    while True:
        user = input("user:")
        passwd = input("passwd:")
        if sgin(c, user, passwd):
            break
    c.close()
