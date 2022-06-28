import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def task(idx):
    print(idx)
    time.sleep(2)


# 内部最多可以有10个线程的线程池
pool = ThreadPoolExecutor(10)

# 往线程池中发任务，1000个任务
for i in range(1000):
    pool.submit(task, i)

# 等待线程池将所有的任务执行完毕
pool.shutdown()

print("执行完毕")
