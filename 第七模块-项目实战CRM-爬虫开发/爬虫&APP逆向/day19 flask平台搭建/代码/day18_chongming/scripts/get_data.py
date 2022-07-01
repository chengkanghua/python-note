import redis

# redis连接池
REDIS_POOL = redis.ConnectionPool(host='127.0.0.1', port=6379, password="qwe123", encoding='utf-8', max_connections=100)

# 在redis连接池中获取连接，再去做操作
conn = redis.Redis(connection_pool=REDIS_POOL)

# 根据连接再去做操作
data = conn.brpop("YANG_VIDEO_TASK", timeout=10)
print(data)
