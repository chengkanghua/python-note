
import redis
pool = redis.ConnectionPool(host='10.211.55.6', port=6379)
r = redis.Redis(connection_pool=pool)



# r.set("name","alex",5)  # 5秒过期
# r.setnx('name','alex') # name不存在时候 才执行设置操作，
# r.set('name','alex2',ex=5) # 5秒过期
# r.setex('name',5,'eric')  # 5秒过期
# r.psetex('name',500,'alex3')# 500毫秒过期

# print(r.get("name"))

# r.set("name","alex",nx=True)
# r.set("name","alex")


# 批量设置

r.mset({'k1': 'v1', 'k2': 'v2'})
# r.mset(k1='v1',k2='v2') # 报错取不到k1值
# origin = r.getset('k1','v11') # 设置新值，返回原来的值
# print(origin)
# print(r.mget('k1','k2'))
# 取值操作

# print(r.get("k2")) # b'v2'

# 批量取值

# print(r.mget(["k1","k2"])) # [b'v1', b'v2']

r.set('name','alexissb')
# print(r.getrange("name",0,2)) # 范围取值 ale

# r.setrange("name",3,"!!!")  # ale!!!sb
# print(r.strlen("name"))  # 打印长度


# r.incr("age",2) # 自增2
# r.decr('age',1)   #自减1
# r.append("name","egon") # 字符串后面增加egon


