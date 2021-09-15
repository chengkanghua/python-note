import time
import random
from concurrent.futures import ThreadPoolExecutor, Future


def task(video_url):
    print("开始执行任务", video_url)
    time.sleep(2)
    return random.randint(0, 10)


# 创建线程池，最多维护10个线程。
pool = ThreadPoolExecutor(10)

future_list = []

url_list = ["www.xxxx-{}.com".format(i) for i in range(15)]
for url in url_list:
    # 在线程池中提交一个任务，线程池中如果有空闲线程，则分配一个线程去执行，执行完毕后再将线程交还给线程池；如果没有空闲线程，则等待。
    future = pool.submit(task, url)
    future_list.append(future)

pool.shutdown(True)
# print('------------------')
for fu in future_list:
    print(fu.result())