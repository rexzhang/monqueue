========
MonQueue
========

MonQueue is a Python library that allows you to use MongoDB as a (FIFO)message queue. Using MonQueue looks a little bit like this…

Create a queue:

    >>> from monqueue import MonQueue
    >>> queue = MonQueue('testqueue')

Put one message into the queue:

    >>> queue.put('it is a message')
    >>> queue.put({'name': 'Rex Zhang', 'city': 'Chengdu', 'country': 'China'})
    >>> queue.put([1, 2, 3])

Get the queue's size:

    >>> queue.qsize()
    3

Peek oldest message info from the queue, just peek, no pop:

    >>> queue.peek()
    (u'it is a message', datetime.datetime(2015, 1, 11, 7, 3, 57, tzinfo=<bson.tz_util.FixedOffset object at 0x0000000002708630>))

Get one message from queue and remove it:

    >>> queue.get()
    u'it is a message'
    >>> queue.get()
    {u'city': u'Chengdu', u'name': u'Rex Zhang', u'country': u'China'}

Check the queue, return True if the queue empty:

    >>> queue.qsize()
    2
    >>> queue.empty()
    False

Clear the queue:

    >>> queue.clear()
    >>> queue.empty()
    True


Installation
============

To install it, just run:

.. code-block:: console

    pip install -U monqueue


Documentation
=============

.. toctree::
    :maxdepth: 2

    apireference
    changelog


Requirements
============

- Python (tested on version 2.7.8)
- `MongoDB <http://www.mongodb.org/>`_
- `pymongo <https://pypi.python.org/pypi/pymongo/>`_