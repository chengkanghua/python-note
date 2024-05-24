import redis

conn = redis.Redis(host='127.0.0.1', port=6379, password="qwe123")

while True:
    # 消费者，去队列中获取数据，如果没有任务默认是返回 None
    v = conn.brpop("video_order_list")
    print(v)
