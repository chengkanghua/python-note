
import redis
pool = redis.ConnectionPool(host='10.211.55.6', port=6379)
r = redis.Redis(connection_pool=pool)

# r.lpush("scores",56,78,99,65,34)
# print(r.lrange("scores",0,4)) #[b'34', b'65', b'99', b'78', b'56']
# print(r.llen('scores'))
# r.rpush("new_scores",23,56,77)
# r.rpushx('new_scores',11) # 当new_scores值存在时候才右边插入11
# print(r.lrange("new_scores",0,5)) #[b'23', b'56', b'77']


# 打印列表所有值
# print(r.lrange("scores",0,-1)) # [b'34', b'65', b'99', b'78', b'56']
# print(r.lrange("new_scores",0,-1)) # [b'23', b'56', b'77']

# r.lpushx("scores",100)

# print(r.llen("scores"))

# 在34值的后面插入44
# r.linsert("scores","AFTER","34","44")

# 对1号索引重新赋值98
# r.lset("scores",1,98)

# 删除98
# r.lrem("scores",count=0,value=98)

# 左侧删除第一个值 并返回删除的值
# print(r.lpop("scores"))
# print(r.lrange("scores",0,-1))
# 返回 索引3的值
# print(r.lindex("scores",3))


# print(r.lrange("scores",0,-1))
# print(r.lrange("scores",1,3))

# 移除索引1-3 之外的所有值
r.ltrim("scores",1,3)
# print(r.lrange("scores",0,-1))



















