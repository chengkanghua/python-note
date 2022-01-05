import time
#导入线程池模块对应的类
from multiprocessing.dummy import Pool
#使用线程池方式执行
start_time = time.time()
def get_page(str):
    print("正在下载 ：",str)
    time.sleep(2)
    print('下载成功：',str)

name_list =['xiaozi','aa','bb','cc']

#实例化一个线程池对象
pool = Pool(4)  # 开辟了4个线程池对象
#将列表中name_list列表每一个元素传递给get_page进行处理。
pool.map(get_page,name_list)
pool.close()

pool.join()  # 等待当前线程的任务执行完毕后再向下继续执行。
end_time = time.time()
print(end_time-start_time)



