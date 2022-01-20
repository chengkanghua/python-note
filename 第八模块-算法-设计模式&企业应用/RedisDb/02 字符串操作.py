
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)



# r.set("name","alex",5)

# print(r.get("name"))

# r.set("name","alex",nx=True)
# r.set("name","alex")


# 批量设置

# r.mset({'k1': 'v1', 'k2': 'v2'})

# 取值操作

# print(r.get("k2")) # b'v2'

# 批量取值

# print(r.mget(["k1","k2"])) # [b'v1', b'v2']


# print(r.getrange("name",0,2))

# r.setrange("name",3,"!!!")

# print(r.strlen("name"))


# r.incr("age",2)

# r.append("name","egon")


