
import redis
pool = redis.ConnectionPool(host='10.211.55.6', port=6379)
r = redis.Redis(connection_pool=pool)


# r.zadd("z",{"n1":1,"n2":2,"n3":5,"n4":3})

# 所有key value
# print(r.zscan("z"))
# 有序集合元素数量
# print(r.zcard("z"))


# print(r.zcount("z",1,3)) # 1到3之间一共3个
# print(r.zcount("z",1,4)) # 1到4 之间 没有4 一共3个
# print(r.zcount("z",1,5)) # 1到5一共4个

# n3自增2
# r.zincrby("z",2,"n3")
# print(r.zscan("z"))

# 按下标去key
# print(r.zrange("z",0,2))
# print(r.zrange("z",0,3))

# 取n4的分数
# print(r.zscore("z","n4"))
# 取n4的下标数字
# print(r.zrank("z","n4"))


# 删除n2
# r.zrem("z","n2")

# r.zremrangebyrank("z",0,1)  # 删除 0 1 索引
# r.zremrangebyscore("z",1,7) # 1-7 分都删除的
# print(r.zscan("z"))




r.zadd("z1",{"n1":1,"n2":2,"n3":3,"x":100})
r.zadd("z2",{"n3":4,"n5":5,"n6":6,"x":100})

# z1 和z2的并集 相同的key值相加
# r.zunionstore("z3",("z1","z2"))
# print(r.zscan("z3"))

# z1和z2的交集，相同的key值相加
r.zinterstore("z4",("z1","z2"))
print(r.zscan("z4"))





















