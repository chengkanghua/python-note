import os
import asyncio
import time
import aiohttp
import requests
from multiprocessing import Process
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

if not os.path.exists('./libs'):
    os.mkdir('./libs')


async def get_request(url):
    """ 基于aiohttp实现的异步协程对象(一组操作集) """
    async with aiohttp.ClientSession() as session:
        async with await session.request(method='get', url=url, headers=headers) as response:
            result = await response.read()
            return result


def task_callback(cb):
    """
    任务对象的回调函数，该回调函数有且只有一个参数
    :param cb: 该回调函数的调用者，即任务对象
    :return:
    """
    path = f'./libs/{time.time()}.jpg'
    with open(path, 'wb') as f:
        f.write(cb.result())
        print(path, '下载成功')


def work(page_url):
    """
    一个线程负责一个页面，从这个页面中提取所有待下载的图片地址
    然后通过异步的方式请求图片地址并下载到本地
    """
    print(page_url)
    page_text = requests.get(url=page_url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')
    img_url_list = []
    for li in li_list:
        img_src = 'http://pic.netbian.com' + li.xpath('./a/img/@src')[0]
        img_url_list.append(img_src)
    print(111, img_url_list)
    # 创建任务对象列表
    task_list = []
    for url in img_url_list:
        cor_obj = get_request(url)
        task_obj = asyncio.ensure_future(cor_obj)
        task_obj.add_done_callback(task_callback)
        task_list.append(task_obj)

    # 创建事件循环对象
    loop = asyncio.get_event_loop()
    # 必须使用wait对task_list进行封装，或者就记住是固定写法即可
    loop.run_until_complete(asyncio.wait(task_list))


if __name__ == '__main__':
    stat = time.time()
    # 创建任务列表，即要爬取的url
    for i in range(2, 5):
        url = 'http://pic.netbian.com/4kmeinv/index_{}.html'.format(i)
        p = Process(target=work, args=(url,))
        p.start()
        p.join()
    print('总耗时: ', time.time() - stat)