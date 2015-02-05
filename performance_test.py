#!/usr/bin/env python
# -*- coding:utf-8 -*-
import time
import monqueue
import hotqueue

def monqueue_test(num):
  print 'monqueue_test'

  
  MSG = {
      'test': "good good",
  }

  queue = monqueue.MonQueue('testqueue', port=27017)

  st = time.time()
  tic = lambda: 'at seconds %s' % (time.time()-st)

  for i in xrange(num):
    queue.put(MSG)

  print 'monqueue put %s times %s' % (num,tic())

  
  st = time.time()
  tic = lambda: 'at seconds %s' % (time.time()-st)
  for i in xrange(num):
    queue.get()

  print 'monqueue get %s times %s' % (num,tic())

def hotqueue_test(num):

  print 'hotqueue_test:'
  MSG = {
      'test': "haha",
  }
  queue = hotqueue.HotQueue("testqueue", host="127.0.0.1", port=6379, db=10)

  st = time.time()
  tic = lambda: 'at seconds %s' % (time.time()-st)

  for i in xrange(num):
    queue.put(MSG)

  ct = time.time() - st

  print 'hotqueue put %s times %s' % (num,tic())
  

  st = time.time()
  tic = lambda: 'at seconds %s' % (time.time()-st)
  for i in xrange(num):
    queue.get()

  ct = time.time() - st
  print 'hotqueue get %s times %s' % (num,tic())

if __name__ == '__main__':

  monqueue_test(10000)
  print '\n---------------------------\n'
  hotqueue_test(10000)
