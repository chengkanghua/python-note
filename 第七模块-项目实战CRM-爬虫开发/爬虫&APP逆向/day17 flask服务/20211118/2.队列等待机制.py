import queue

q = queue.Queue()
while True:
    try:
        # 代码队列中是否有数据，最多等待10s
        data = q.get(block=True, timeout=10)
        print(data)
    except queue.Empty as e:
        print("等待10s，队列依然没数据")
