#!/usr/bin/env python
#coding=utf-8


from __future__ import print_function, unicode_literals, absolute_import

import time
import monqueue
import hotqueue


MSG = {
    'test': "good good",
}


def monqueue_test(num):
    print('monqueue_test')

    queue = monqueue.MonQueue('testqueue', port=27017)

    #
    st = time.time()
    tic = lambda: 'at seconds %s' % (time.time()-st)
    for i in xrange(num):
        queue.put(MSG)

    print('monqueue put %s times %s' % (num,tic()))

    #
    st = time.time()
    tic = lambda: 'at seconds %s' % (time.time()-st)
    for i in xrange(num):
        queue.peek()

    print('monqueue peek %s times %s' % (num,tic()))

    #
    st = time.time()
    tic = lambda: 'at seconds %s' % (time.time()-st)
    for i in xrange(num):
        queue.get()

    print('monqueue get %s times %s' % (num,tic()))


def hotqueue_test(num):
    print('hotqueue_test:')

    queue = hotqueue.HotQueue("testqueue", host="127.0.0.1", port=6379, db=10)

    st = time.time()
    tic = lambda: 'at seconds %s' % (time.time()-st)

    for i in xrange(num):
        queue.put(MSG)

    ct = time.time() - st

    print('hotqueue put %s times %s' % (num,tic()))


    st = time.time()
    tic = lambda: 'at seconds %s' % (time.time()-st)
    for i in xrange(num):
        queue.get()

    ct = time.time() - st
    print('hotqueue get %s times %s' % (num,tic()))


if __name__ == '__main__':
    monqueue_test(10000)
    print('\n---------------------------\n')
    hotqueue_test(10000)
