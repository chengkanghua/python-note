
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)


# r.hset("infos","name","alex")

# r.hmset("infos",{"age":1000,"gender":"male"})

# print(r.hget("infos","name"))

# print(r.hmget("infos",["name","age"])) # [b'alex', b'1000']

# print(r.hgetall("infos")) # {b'name': b'alex', b'age': b'1000', b'gender': b'male'}

# print(r.hlen("infos"))

# print(r.hkeys("infos")) # [b'name', b'age', b'gender']
# print(r.hvals("infos")) # [b'alex', b'1000', b'male']
#
# print(r.hexists("infos","names"))

# r.hdel("infos","gender")
# print(r.hgetall("infos")) # {b'name': b'alex', b'age': b'1000'}

# r.hincrby("infos","age",2)

# print(r.hgetall("infos"))

# print(r.hscan_iter("infos"))
#
# for i in r.hscan_iter("infos"):
#     print(i)


# r.hmset("abc",{"a1":"b1","a2":"b2","a3":"b3","x1":"y1"})


for i in r.hscan_iter("abc",match="a*"):
    print(i)



















