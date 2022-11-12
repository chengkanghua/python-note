from multiprocessing import Process, Lock
import time


def task(name,mutex):
    mutex.acquire()
    print('%s 1' % name)
    time.sleep(1)
    print('%s 2' % name)
    time.sleep(1)
    print('%s 3' % name)
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    for i in range(3):
        p = Process(target=task, args=('进程%s' % i, mutex))
        p.start()
