
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)


# r.zadd("z",{"n1":1,"n2":2,"n3":5,"n4":3})

# print(r.zscan("z"))
#
# print(r.zcard("z"))


# print(r.zcount("z",1,3))
# print(r.zcount("z",1,4))
# print(r.zcount("z",1,5))

# r.zincrby("z",2,"n3")
# print(r.zscan("z"))

# print(r.zrange("z",0,2))
# print(r.zrange("z",0,3))

# print(r.zscore("z","n4"))
# print(r.zrank("z","n4"))



# r.zrem("z","n2")

# r.zremrangebyrank("z",0,1)
# r.zremrangebyscore("z",1,7)
# print(r.zscan("z"))




# r.zadd("z1",{"n1":1,"n2":2,"n3":3,"x":100})
# r.zadd("z2",{"n3":4,"n5":5,"n6":6,"x":100})

# r.zunionstore("z3",("z1","z2"))
# print(r.zscan("z3"))

r.zinterstore("z4",("z1","z2"))
print(r.zscan("z4"))





















