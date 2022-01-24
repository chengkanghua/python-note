
import redis
pool = redis.ConnectionPool(host='10.211.55.6', port=6379)
r = redis.Redis(connection_pool=pool)

# 获取k开头的 key
# print(r.keys(pattern="k*"))
# print(r.delete("naem"))
# 打印所有的key
# print(r.keys())

# 是否存在key为name 存在返回1 不存在0
# print(r.exists("name"))
# print(r.exists("naem"))

# 为name设置10秒超时
# r.expire("name",10)
# print(r.keys())

#随机获取一个key
# print(r.randomkey())
# 获取infos对应值的类型
# print(r.type("infos"))  # hash


# 迭代获取 k开头的key
for i in r.scan_iter(match="k*"):
    print(i)



