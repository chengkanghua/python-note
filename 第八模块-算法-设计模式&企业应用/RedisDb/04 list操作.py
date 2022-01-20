
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# r.lpush("scores",56,78,99,65,34)

#r.rpush("new_scores",23,56,77)

# print(r.lrange("scores",0,-1)) # [b'34', b'65', b'99', b'78', b'56']
# print(r.lrange("new_scores",0,-1)) # [b'23', b'56', b'77']

# r.lpushx("scores",100)

# print(r.llen("scores"))

# r.linsert("scores","AFTER","34","44")

# r.lset("scores",1,98)

# r.lrem("scores",count=0,value=98)

# print(r.lrange("scores",0,-1))

# print(r.lpop("scores"))
# print(r.lrange("scores",0,-1))

# print(r.lindex("scores",3))


# print(r.lrange("scores",0,-1))
# print(r.lrange("scores",1,3))


# r.ltrim("scores",1,3)
# print(r.lrange("scores",0,-1))



















