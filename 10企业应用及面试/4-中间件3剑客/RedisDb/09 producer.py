import redis

r = redis.Redis(host='10.211.55.6')

# Publish 命令用于将信息发送到指定的频道。
r.publish("fm104.5", "Hi,yuan!")