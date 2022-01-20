
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)

# print(r.keys(pattern="k*"))
# print(r.delete("naem"))
# print(r.keys())


# print(r.exists("name"))
# print(r.exists("naem"))


# r.expire("name",10)
# print(r.keys())
#
# print(r.randomkey())
#
# print(r.type("infos"))


for i in r.scan_iter(match="k*"):
    print(i)



