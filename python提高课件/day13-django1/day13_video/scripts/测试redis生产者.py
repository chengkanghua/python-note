import redis

conn = redis.Redis(host='127.0.0.1', port=6379, password="qwe123")
# 在队列中存放数据
conn.lpush("video_order_list", "2021111111111")
conn.lpush("video_order_list", "33333333333")

