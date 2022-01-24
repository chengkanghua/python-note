
import redis
pool = redis.ConnectionPool(host='10.211.55.6', port=6379)
r = redis.Redis(connection_pool=pool)


# r.sadd("score_set01",1,2,3,4,5,6,6)
# print(r.scard("score_set01")) # 去重返回元素总个数
# r.sadd("score_set02",4,5,6,7,8)


print(r.smembers("score_set01")) #获取 score_set01所有成员
print(r.smembers("score_set02"))

# # 去重返回元素总个数
# print(r.scard("score_set01"))
# print(r.scard("score_set02"))
#
print(r.sinter("score_set01","score_set02")) # 交集     - 你有我也有的
# print(r.sunion("score_set01","score_set02"))  # 并集  -加一起去重
print(r.sdiff("score_set01","score_set02"))  # 差集     - 我有  你没有的
#
#
#
# print(r.sismember("score_set01",6)) # 6是否是score_set01的集合
# print(r.sismember("score_set01",7))

# 集合中随机移除一个成员，并返回
# print(r.spop("score_set01"))
# print(r.smembers("score_set01"))

# 随机获取3个数
# print(r.srandmember("score_set01",3))

# 删除3
# r.srem("score_set01",3)
# print(r.smembers("score_set01"))

# # 返回迭代器，
# print(r.sscan_iter("score_set01"))
# for i in r.sscan_iter("score_set01"):
#     print(i)


















