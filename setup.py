#!/usr/bin/env python
#coding=utf-8


import os
from setuptools import setup, find_packages


rel_file = lambda *args: os.path.join(os.path.dirname(os.path.abspath(__file__)), *args)


def read_from(filename):
    fp = open(filename)
    try:
        return fp.read()
    finally:
        fp.close()

def get_long_description():
    return read_from(rel_file('README.rst'))

def get_version():
    import monqueue
    return monqueue.__version__


setup(
    name='MonQueue',
    version=get_version(),
    description='MonQueue is a Python library that allows you to use MongoDB as a message queue.',
    long_description=get_long_description(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='queue mongodb',

    author='Rex Zhang',
    author_email='rex.zhang@gmail.com',
    url='https://github.com/rexzhang/monqueue',
    license='LGPL',

    py_modules=['monqueue'],
    install_requires=['pymongo', ],
)