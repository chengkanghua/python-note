import utils
import time
import threading
from concurrent.futures import ThreadPoolExecutor

EXEC_STOP_STATUS = False

EXEC_COUNT = 0
LOCK = threading.RLock()


def task(url):
    if EXEC_STOP_STATUS:
        return

    # B站、抖音、x视频
    print("执行任务", url)

    time.sleep(2)
    with LOCK:
        global EXEC_COUNT
        EXEC_COUNT += 1


def stop_task():
    while True:
        txt = input("输入q/Q终止：")
        if txt.upper() == "Q":
            global EXEC_STOP_STATUS
            EXEC_STOP_STATUS = True
            break


def run():
    # 刚启动时，应该找到所有的中断执行的订单（重新加入到队列）
    utils.db_retry_stop_task()

    # 创建线程
    t = threading.Thread(target=stop_task)
    t.start()

    while True:
        if EXEC_STOP_STATUS:
            return

        # 1.去消息队列中获取任务（订单号）
        oid = utils.redis_get_task(10)
        if not oid:
            continue
        print("开始执行订单：", oid)

        # 2.更新订单信息（正在执行）
        utils.db_update_task_status(oid, 2)

        # 3.执行任务
        # 3.1 获取订单的信息：count，URL
        order_dict = utils.db_get_task_info(oid)
        total_count = int(order_dict['count'])
        exec_count = int(order_dict['exec_count'])
        count = total_count - exec_count

        video_url = order_dict['url']

        # 3.2 开始刷（最开始带着大家写的脚本）
        pool = ThreadPoolExecutor(20)
        for _ in range(count):
            pool.submit(task, video_url)
        pool.shutdown()

        # 4.执行完毕（更新订单）
        if EXEC_STOP_STATUS:
            # 用户主动终止
            utils.db_update_task_status_stop(oid, 4, EXEC_COUNT)
            return
        else:
            # 正常结束
            utils.db_update_task_status_stop(oid, 3, EXEC_COUNT)


if __name__ == '__main__':
    run()
