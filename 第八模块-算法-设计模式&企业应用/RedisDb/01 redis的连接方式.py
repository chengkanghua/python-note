

import redis
# 01 基本连接方式
# r=redis.Redis(host="127.0.0.1",port=6379)
#
#
# r.set("age",99)
#
# print(r.get("age")) # b'99'



# 02 基于连接池连接
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)



