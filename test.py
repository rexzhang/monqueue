#!/usr/bin/env python
#coding=utf-8


import unittest

from monqueue import MonQueue


multi_queue_in_one_coll = False

MSG = {
    'test': "haha",
}


class MonQueueTestCase(unittest.TestCase):

    #----------------------------------------------------------------------
    def setUp(self):
        """Create the queue instance before the test."""
        self.queue = MonQueue('testqueue', port=9005)
        return

    #----------------------------------------------------------------------
    def tearDown(self):
        """Clear the queue after the test."""
        self.queue.clear()
        return

    #----------------------------------------------------------------------
    def test_put_peek_get(self):
        """Test put and get method."""
        msg_put = MSG
        self.queue.put(msg_put)

        msg_peek, timestamp = self.queue.peek()
        self.assertEqual(msg_put, msg_peek)

        msg_get = self.queue.get()
        self.assertEqual(msg_put, msg_get)

        return

    #----------------------------------------------------------------------
    def test_qsize_clear_empty(self):
        """"""
        msg_put = MSG
        self.queue.put(msg_put)

        self.assertEqual(self.queue.qsize(), len(MSG))

        self.queue.clear()
        self.assertEqual(self.queue.qsize(), 0)

        self.assertEqual(self.queue.empty(), True)

        return

class MonQueueTestCase_multi_queue_in_one_coll(MonQueueTestCase):
    #----------------------------------------------------------------------
    def setUp(self):
        """test multi_queue_in_one_coll mode"""
        self.queue = MonQueue('testqueue', port=9005, multi_queue_in_one_coll=True)
        return


if __name__ == "__main__":
    unittest.main()

