
import redis
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
r = redis.Redis(connection_pool=pool)



print(r.keys())


# pipe = r.pipeline(transaction=True)
#
# pipe.set('name', 'alex')
# xxxx
# pipe.set('role', 'sb')
#
# pipe.execute()