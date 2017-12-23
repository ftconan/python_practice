# coding=utf-8

import time, threading, multiprocessing


def loop():
    """新线程执行的代码"""
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n += 1
        print 'thread %s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print 'thread %sw ended.' % threading.current_thread().name


# 假定这是你的银行存款：
balance = 0
lock = threading.Lock()


def change_it(n):
    """
    先存后取，结果应该为0
    :param n:
    :return:
    """
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(100000):
        # 先要获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 改完释放锁
            lock.release()


def loop():
    x = 0
    while True:
        x ^= 1


# 创建全局T和readLocal对象
local_school = threading.local()


def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)


def process_thread(name):
    """
    绑定ThreadLocal的student
    :param name:
    :return:
    """
    local_school.student = name
    process_student()


if __name__ == '__main__':
    # t = threading.Thread(target=loop, name='LoopThread')
    # t.start()
    # t.join()
    # print 'thread %s ended.' % threading.current_thread().name

    # t1 = threading.Thread(target=run_thread, args=(5,))
    # t2 = threading.Thread(target=run_thread, args=(8,))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # print balance

    # print multiprocessing.cpu_count()
    # for i in range(multiprocessing.cpu_count()):
    #     t = threading.Thread(target=loop)
    #     t.start()

    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
