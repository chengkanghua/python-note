import requests,asyncio,time

start = time.time()
# 运行此文件 , 先运行flask服务.py 文件
urls = [
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
]
async def request(url):
    print('正在下载..',url)
    # requests.get是基于同步，必须使用基于异步的网络请求模块进行指定url的请求发送
    # aiohttp:基于异步网络请求的模块   引出下一节
    response = requests.get(url=url)
    print('下载完成',response.text)

tasks = []

for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print(end-start)  # 6.043938159942627
