import asyncio
import time
# 协程函数
async def request(url):
    print('正在下载',url)
    await asyncio.sleep(2)
    print('下载完毕',url)

start = time.time()

urls = [
    'www.baidu.com',
    'www.sogou.com',
    'www.qq.com',
]

stasks = []   # 存放多个任务
for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop = asyncio.get_event_loop()  # 事件循环对象
loop.run_until_complete(asyncio.wait(stasks))  # task对象交给loop对象处理

end = time.time()
print(end-start)



