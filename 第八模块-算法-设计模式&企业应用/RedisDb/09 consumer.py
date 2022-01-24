import redis

r = redis.Redis(host='10.211.55.6')
# Pubsub 命令用于查看订阅与发布系统状态
pub = r.pubsub()

# Subscribe 命令用于订阅给定的一个或多个频道的信息。。
pub.subscribe("fm104.5")
pub.parse_response()

while 1:
    msg = pub.parse_response()
    print(msg)
