#!/usr/bin/env python
# coding=utf-8


import time
import monqueue
import hotqueue


MSG = {
    'test': "good good",
}


def monqueue_test(times):
    print('MonQueue test:')

    queue = monqueue.MonQueue('test_queue')

    start_time = time.time()
    for i in range(times):
        queue.put(MSG)
    print('MonQueue put {} times in {} seconds'.format(times, time.time() - start_time))

    start_time = time.time()
    for i in range(times):
        queue.peek()
    print('MonQueue peek {} times in {} seconds'.format(times, time.time() - start_time))

    start_time = time.time()
    for i in range(times):
        queue.get()
    print('MonQueue get {} times in {} seconds'.format(times, time.time() - start_time))

    return


def hotqueue_test(times):
    print('HotQueue test:')

    queue = hotqueue.HotQueue("test_queue", host="127.0.0.1", port=6379, db=10)

    start_time = time.time()
    for i in range(times):
        queue.put(MSG)
    print('HotQueue put {} times in {} seconds'.format(times, time.time() - start_time))

    start_time = time.time()
    for i in range(times):
        queue.get()
    print('HotQueue get {} times in {} seconds'.format(times, time.time() - start_time))

    return


if __name__ == '__main__':
    monqueue_test(10000)
    hotqueue_test(10000)
