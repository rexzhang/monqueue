#!/usr/bin/env python
#coding=utf-8


import pymongo


__version__ = "0.1"


QUEUE_LABLE_NAME = 'q'
QUEUE_LABLE_MSG = 'm'


########################################################################
class MonQueue(object):
    """MonQueue is a Python library that allows you to use MongoDB as a message queue"""

    #----------------------------------------------------------------------
    def __init__(self, name, host='localhost', port=27017, db_name='queue', coll_name=None, multi_queue_in_one_coll=False):
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
        """put one message to queue. Example:

        >>> queue.put("first message")
        >>> queue.put("2nd message)

        """
        if self.__multi_queue_in_one_coll:
            self.__coll.insert({
                QUEUE_LABLE_NAME: self.name,
                QUEUE_LABLE_MSG: msg,
            })
        else:
            self.__coll.insert({
                QUEUE_LABLE_MSG: msg,
            })

        return

    #----------------------------------------------------------------------
    def get(self):
        """get one message and remove it"""
        msg = self.__coll.find_and_modify(query=self.__query, sort=[('_id', pymongo.ASCENDING)], remove=True)

        if msg != None:
            msg = msg[QUEUE_LABLE_MSG]

        return msg

    #----------------------------------------------------------------------
    def peek(self):
        """peek oldest message info
        just peek, no pop
        """
        timestamp = None

        msg = self.__coll.find_one(query=self.__query, sort=[('_id', pymongo.ASCENDING)])

        if msg != None:
            timestamp = msg['_id'].generation_time
            msg = msg[QUEUE_LABLE_MSG]

        return msg, timestamp

    #----------------------------------------------------------------------
    def qsize(self):
        """get queue' size"""
        if self.__multi_queue_in_one_coll:
            size = self.__coll.find({QUEUE_LABLE_NAME: self.name}).count()
        else:
            size = self.__coll.count()

        return size

    #----------------------------------------------------------------------
    def empty(self):
        """return True, if queue is empty"""
        if self.qsize() == 0:
            return True
        else:
            return False

    #----------------------------------------------------------------------
    def clear(self):
        """clear queue"""
        self.__coll.remove(query=self.__query)

        return



if __name__ == "__main__":
    pass