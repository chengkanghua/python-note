# -------------------- 执行一次 ----------------------
# import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
#
#
# def job2(text):
#     print('job2', datetime.datetime.now(), text)
#
# # 新建一个调度器
# scheduler = BlockingScheduler()
#
# # 新建任务： 2020, 5, 8, 11, 51, 1 表示 在 2020年5月8号11点51分01秒执行一次
# scheduler.add_job(job2, 'date', run_date=datetime.datetime(2020, 5, 8, 11, 51, 1), args=['text'], id='job2')
#
# # 运行任务
# scheduler.start()


# --------------- 间隔执行 ------------------


# import datetime
# from apscheduler.schedulers.blocking import BlockingScheduler
#
# def job1():
#     print('job1', datetime.datetime.now())
# scheduler = BlockingScheduler()
# scheduler.add_job(job1, 'interval', seconds=5, id='job1')  # 每隔5秒执行一次
# scheduler.start()

# ----------------- 每天指定时间 执行一次 -----------------

from apscheduler.schedulers.blocking import BlockingScheduler  # 后台运行

sc = BlockingScheduler()
f = open('t1.txt', 'a', encoding='utf8')

@sc.scheduled_job('cron', day_of_week='*', hour=11, minute='56', second='2')  # 每天11点56分02秒执行一次
def check_db():
    print(111111111111)

if __name__ == '__main__':
    try:
        sc.start()
        f.write('定时任务成功执行')
    except Exception as e:
        sc.shutdown()
        f.write('定时任务执行失败')
    finally:
        f.close()
