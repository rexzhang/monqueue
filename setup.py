#!/usr/bin/env python
#coding=utf-8


from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))


def get_long_description():
    # Get the long description from the relevant file
    with open(path.join(here, 'README.rst')) as f:
        long_description = f.read()

    return long_description

def get_version():
    import monqueue
    return monqueue.__version__


setup(
    name='MonQueue',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=get_version(),

    description='MonQueue is a Python library that allows you to use MongoDB as a message queue.',
    long_description=get_long_description(),

    # The project's main homepage.
    url='https://github.com/rexzhang/monqueue',

    # Author details
    author='Rex Zhang',
    author_email='rex.zhang@gmail.com',

    # Choose your license
    license='LGPL',

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',

        'Operating System :: OS Independent',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # What does your project relate to?
    keywords='queue mongodb',

    # List run-time dependencies here.  These will be installed by pip when your
    # project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['pymongo', ],

    py_modules=['monqueue'],
)