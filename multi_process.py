# coding=utf-8

from multiprocessing import Process
import os

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


if __name__ == '__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
