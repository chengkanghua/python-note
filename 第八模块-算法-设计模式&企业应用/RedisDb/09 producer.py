import redis

r = redis.Redis(host='127.0.0.1')
r.publish("fm104.5", "Hi,yuan!")