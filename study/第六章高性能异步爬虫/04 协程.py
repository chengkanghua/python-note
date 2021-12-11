import asyncio

# async 协程函数
async def request(url):
    print("正在请求的url是",url)
    print('请求成功',url)
    return url

# 返回一个协程对象
c = request('http://www.baidu.com')

# # 获取一个事件循环对象
# loop = asyncio.get_event_loop()
# loop.run_until_complete(c)  # 协程对象注册到loop 里

# task使用
# loop = asyncio.get_event_loop()
# task = loop.create_task(c)
# loop.run_until_complete(task)

# future使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# loop.run_until_complete(task)

def callback_func(task):
    print(task.result())  # result返回的就是任务对象中封装的协程对象对应函数的返回值

loop = asyncio.get_event_loop()
task = loop.create_task(c)
task.add_done_callback(callback_func)
loop.run_until_complete(task)
