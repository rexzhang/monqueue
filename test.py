#!/usr/bin/env python
#coding=utf-8


import unittest
import datetime

from monqueue import MonQueue


multi_queue_in_one_coll = False

MSG = {
    'test': "haha",
}


class MonQueueTestCase(unittest.TestCase):

    #----------------------------------------------------------------------
    def setUp(self):
        """Create the queue instance before the test."""
        self.queue = MonQueue('monqueue_test')
        self.queue.clear()
        return

    #----------------------------------------------------------------------
    def tearDown(self):
        """Clear the queue after the test."""
        self.queue.clear()
        return

    #----------------------------------------------------------------------
    def test_put_get(self):
        """Test put and get method."""
        msg_put = MSG
        self.queue.put(msg_put)

        msg_get = self.queue.get()
        self.assertEqual(msg_put, msg_get)
        return

    #----------------------------------------------------------------------
    def test_peek(self):
        """test peek method"""
        msg_put = MSG
        self.queue.put(msg_put)

        #normal peek
        msg_peek, ext_info = self.queue.peek()
        self.assertEqual(msg_put, msg_peek)

        #peek timestamp
        msg_peek, ext_info = self.queue.peek(timestamp=True)
        self.assertEqual(msg_put, msg_peek)
        if 'timestamp' in ext_info:
            self.assertEqual(type(ext_info['timestamp']), type(datetime.datetime.now()))

        #peek _mongo_id's string
        msg_peek,ext_info = self.queue.peek(mongo_id_str=True)
        self.assertEqual(msg_put, msg_peek)
        if 'mongo_id_str' in ext_info:
            self.assertEqual(type(ext_info['mongo_id_str']), str)
            self.assertEqual(len(ext_info['mongo_id_str']), 24)

        return

    #----------------------------------------------------------------------
    def test_qsize_clear_empty(self):
        """"""
        msg_put = MSG
        self.queue.put(msg_put)

        self.assertEqual(self.queue.qsize(), len(MSG))

        self.queue.clear()
        self.assertEqual(self.queue.qsize(), 0)

        self.assertEqual(self.queue.empty, True)

        return

class MonQueueTestCase_multi_queue_in_one_coll(MonQueueTestCase):
    #----------------------------------------------------------------------
    def setUp(self):
        """test multi_queue_in_one_coll mode"""
        self.queue = MonQueue('monqueue_test', multi_queue_in_one_coll=True)
        return


if __name__ == "__main__":
    unittest.main()

