# 生成激活码的函数
import uuid
def Generate_Code(counts,length=20):
    key_list = []

    for i in range(counts):
        key = str(uuid.uuid4())[:length]
        if key not in key_list:
            key_list.append(key)

    return key_list

import redis

#创建数据库连接
def redis_conn():
    #用线程池的方式减少性能开销
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    return r

#将激活码用List方式储存到Redis数据库
def updata_redis():
    r = redis_conn()
    key = Generate_Code(200)
    for i in key:
        r.rpush("Code",i)
    r.save()

#从Redis读取数据
def getdata():
    r = redis_conn()
    for key in r.lrange("Code",0,-1):
        print(key)

if __name__ == "__main__":
    updata_redis()
    getdata()