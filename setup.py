
import re
from setuptools import setup
import ast

setup(
    name='jolla',
    keywords=['back-end', 'framework', 'RESTful', 'gevent'],
    version='1.1.9',
    description='high performance RESTful framework',
    author='aljun',
    author_email='salamer_gaga@163.com',
    license='Apache',
    url='https://github.com/salamer/jolla',
    download_url='https://github.com/salamer/jolla',

    install_requires=[
        'gevent'
    ],

    packages=['jolla'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        "License :: OSI Approved :: Apache Software License",
        'Environment :: Web Environment',
        "Programming Language :: Python :: 2.7",
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
