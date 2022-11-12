
import redis
pool = redis.ConnectionPool(host='10.211.55.6', port=6379)
r = redis.Redis(connection_pool=pool)



print(r.keys())


# pipe 原子性操作
# pipe = r.pipeline(transaction=True)
# pipe.set('name', 'alex')
# xxxx
# pipe.set('role', 'sb')
# pipe.execute()