
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)



# r.sadd("score_set01",1,2,3,4,5,6,6)
# r.sadd("score_set02",4,5,6,7,8)


# print(r.smembers("score_set01"))
# print(r.smembers("score_set02"))
#
# print(r.scard("score_set01"))
# print(r.scard("score_set02"))
#
# print(r.sinter("score_set01","score_set02")) # 交集
# print(r.sunion("score_set01","score_set02"))  # 并集
# print(r.sdiff("score_set01","score_set02"))  # 差集
#
#
#
# print(r.sismember("score_set01",6))
# print(r.sismember("score_set01",7))

# print(r.spop("score_set01"))
# print(r.smembers("score_set01"))

# print(r.srandmember("score_set01",3))

# r.srem("score_set01",5)
# print(r.smembers("score_set01"))


# print(r.sscan_iter("score_set01"))
# for i in r.sscan_iter("score_set01"):
#     print(i)


















