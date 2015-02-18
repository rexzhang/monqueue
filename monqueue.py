#!/usr/bin/env python
#coding=utf-8


import pymongo
import bson
import time


__version__ = "0.2.2"


QUEUE_LABLE_NAME = 'q'
QUEUE_LABLE_QMSG = 'm'


########################################################################
class MonQueue(object):
    """MonQueue is a Python library that allows you to use MongoDB as a message queue"""

    #----------------------------------------------------------------------
    def __init__(self, name, host='localhost', port=27017, db_name='monqueue', coll_name=None, multi_queue_in_one_coll=False):
        """Constructor

        supprt two mode:
            * one coll one queue
            * one coll multi queue
        """
        if coll_name == None:
            coll_name = name

        self.name = name
        self.__multi_queue_in_one_coll = multi_queue_in_one_coll

        self.__conn = pymongo.MongoClient(host=host, port=port)
        self.__db = pymongo.database.Database(self.__conn, db_name)
        self.__coll = pymongo.collection.Collection(self.__db, coll_name)

        if self.__multi_queue_in_one_coll:
            self.__query = {QUEUE_LABLE_NAME: self.name}

            self.__coll.ensure_index([(QUEUE_LABLE_NAME, 1), ('_id', 1)])
        else:
            self.__query = {}

        return

    #----------------------------------------------------------------------
    def put(self, msg):
        """Put one message into queue. Example:

        >>> queue.put('it is a message')
        >>> queue.put({'name': 'Rex Zhang', 'city': 'Chengdu', 'country': 'China'})
        >>> queue.put([1, 2, 3])
        """
        if self.__multi_queue_in_one_coll:
            self.__coll.insert({
                QUEUE_LABLE_NAME: self.name,
                QUEUE_LABLE_QMSG: msg,
            })
        else:
            self.__coll.insert({
                QUEUE_LABLE_QMSG: msg,
            })

        return

    #----------------------------------------------------------------------
    def get(self, block=True, timeout=None):
        """Get one message from queue and remove it.

        :param block: blocking mode
        :param timeout: depend block mode

        >>> queue.get()
        u'it is a message'
        >>> queue.get()
        {u'city': u'Chengdu', u'name': u'Rex Zhang', u'country': u'China'}

        :TODO: raise Empty
        """
        #init default return value
        msg = None

        if not block:
            doc = self.__coll.find_and_modify(query=self.__query, sort=[('_id', pymongo.ASCENDING)], remove=True)

        elif timeout is None:
            doc = None
            while doc is None:
                doc = self.__coll.find_and_modify(query=self.__query, sort=[('_id', pymongo.ASCENDING)], remove=True)

        elif timeout < 0:
            raise ValueError("'timeout' must be a non-negative number")

        else:
            stop_time = time.time() + timeout
            while True:
                doc = self.__coll.find_and_modify(query=self.__query, sort=[('_id', pymongo.ASCENDING)], remove=True)

                if doc == None and stop_time > time.time():
                    time.sleep(1)
                else:
                    break

        if doc != None:
            msg = doc[QUEUE_LABLE_QMSG]

        return msg

    #----------------------------------------------------------------------
    def peek(self, timestamp=False, mongo_id_str=False):
        """Peek oldest message info. just peek, no pop.

        :rtype: (message object, dict object)

        >>> q.put('queue msg')
        >>> q.peek()
        ('queue msg', {})
        >>> q.peek(timestamp=True)
        ('queue msg', {'timestamp': datetime.datetime(2015, 2, 4, 5, 58, 37, tzinfo=<bson.tz_util.FixedOffset object at 0x101389d90>)})
        >>> q.peek(mongo_id_str=True)
        ('queue msg', {'mongo_id_str': '54d1b50ddd7215c3b15ed992'})
        """
        ext_info = {}

        doc = self.__coll.find_one(query=self.__query, sort=[('_id', pymongo.ASCENDING)])

        if doc != None:
            msg = doc[QUEUE_LABLE_QMSG]

            if timestamp:
                ext_info['timestamp'] = doc['_id'].generation_time

            if mongo_id_str:
                ext_info['mongo_id_str'] = str(bson.objectid.ObjectId(doc['_id'].binary))

        return msg, ext_info

    #----------------------------------------------------------------------
    def qsize(self):
        """Get the queue's size.

        :rtype: int
        """
        if self.__multi_queue_in_one_coll:
            size = self.__coll.find({QUEUE_LABLE_NAME: self.name}).count()
        else:
            size = self.__coll.count()

        return size

    #----------------------------------------------------------------------
    @property
    def empty(self):
        """Check the queue, return True if the queue empty.

        :rtype: True or False
        """
        if self.qsize() == 0:
            return True
        else:
            return False

    #----------------------------------------------------------------------
    def clear(self):
        """clear the queue"""
        self.__coll.remove(query=self.__query)

        return



if __name__ == "__main__":
    pass
