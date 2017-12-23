# coding=utf-8

from multiprocessing import Process, Pool, Queue
import os, time, random

# print 'Process (%s) start...' % os.getpid()
# pid = os.fork()
# if pid==0:
#     print 'I am child process(%s) and my parent is %s.' % (os.getpid(), os.getppid())
# else:
#     print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)


def run_proc(name):
    """
    子进程要执行的代码
    :param name:
    :return:
    """
    print 'Run child process %s (%s)...' %(name, os.getpid())


def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))


def write(q):
    """
    写数据进程执行的代码
    :param q:
    :return:
    """
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


def read(q):
    """
    读数据进程执行的代码
    :param q:
    :return:
    """
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value


if __name__ == '__main__':
    # print 'Parent process %s.' % os.getpid()
    # p = Process(target=run_proc, args=('test',))
    # print 'Process will start.'
    # p.start()
    # p.join()
    # print 'Process end.'

    # print 'Parent process %s.' % os.getpid()
    # p = Pool()
    # for i in range(9):
    #     p.apply_async(long_time_task, args=(i,))
    # print 'Waiting for all subprocesses done...'
    # p.close()
    # p.join()
    # print 'All subprocesses done.'

    # 父进程创建Queue,并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
