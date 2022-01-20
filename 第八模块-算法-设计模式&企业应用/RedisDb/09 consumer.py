import redis

r = redis.Redis(host='127.0.0.1')
pub = r.pubsub()

pub.subscribe("fm104.5")
pub.parse_response()

while 1:
    msg = pub.parse_response()
    print(msg)
