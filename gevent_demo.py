# coding=utf-8

from gevent import monkey; monkey.patch_socket()
import gevent
import urllib2


def f(n):
    for i in range(n):
        print gevent.getcurrent(), i
        gevent.sleep(0)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()


def f1(url):
    print ('GET: %s' % url)
    resp = urllib2.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
    gevent.spawn(f1, 'https://www.python.org/'),
    gevent.spawn(f1, 'https://www.yahoo.org/'),
    gevent.spawn(f1, 'https://github.org/'),
])