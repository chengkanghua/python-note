
import redis
pool = redis.ConnectionPool(host='10.211.55.6', port=6379)
r = redis.Redis(connection_pool=pool)


# r.hset("infos","name","alex")
# print(r.hget('infos','name')) # 获取hash infos 里name的值

# 批量设置
r.hmset("infos",{"age":1000,"gender":"male"})
# print(r.hmget('infos','age','gender')) # 获取多个值
# print(r.hmget("infos",["name","age"])) # [b'alex', b'1000']

# print(r.hgetall("infos")) # {b'name': b'alex', b'age': b'1000', b'gender': b'male'}

# print(r.hlen("infos")) # hash中键值对的个数

# print(r.hkeys("infos")) # [b'name', b'age', b'gender'] 所有keys
# print(r.hvals("infos")) # [b'alex', b'1000', b'male']  所有vaules
#
# print(r.hexists("infos","names")) #是否存在names 的key

# r.hdel("infos","gender")   # 删除指定的key 的键值对
# print(r.hgetall("infos")) # {b'name': b'alex', b'age': b'1000'}

# r.hincrby("infos","age",2) # age自增2

# print(r.hgetall("infos"))

# print(r.hscan_iter("infos")) # 返回迭代器
# for i in r.hscan_iter("infos"):
#     print(i)


# r.hmset("abc",{"a1":"b1","a2":"b2","a33":"b33","x1":"y1"})
r.hset('abc',mapping={"a1":"b1","a2":"b2","a33":"b33","x1":"y1"}) # 新方式

for i in r.hscan_iter("abc",match="a*"): # 匹配key是a开头的
    print(i)



















