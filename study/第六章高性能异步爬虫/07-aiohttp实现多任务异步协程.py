import requests,asyncio,time,aiohttp

start = time.time()
# 运行此文件 , 先运行flask服务.py 文件
urls = [
    'http://127.0.0.1:5000/bobo','http://127.0.0.1:5000/jay','http://127.0.0.1:5000/tom'
]
async def get_page(url):
    async with aiohttp.ClientSession() as session:
        async with await session.get(url=url) as response:
            page_txt = await response.text()
            print(page_txt)

tasks = []

for url in urls:
    c = get_page(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print(end-start)  # 6.043938159942627
