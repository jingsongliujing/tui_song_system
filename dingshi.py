'''
操作系统定时任务
'''
import datetime
import time
from apscheduler.schedulers.background import BackgroundScheduler
import os


def timedTask():
    val = os.system('python kc.py')
    val2 = os.system('python kaoshi.py')
    print(val)
    print(val2)
    print(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])


if __name__ == '__main__':
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()

    # 添加调度任务
    # 调度方法为 timedTask，触发器选择 interval(间隔性)，间隔时长为 2 秒,侧式时候用seconeds,minutes,hours关键字替换定时任务
    scheduler.add_job(timedTask, 'interval', minutes=5)
    # 启动调度任务
    scheduler.start()

    while True:
        print(time.time())
        time.sleep(10)
