#!/usr/bin/env python

from setuptools import setup

setup(
    name='dtx-examples',
    version='0.9.3',
    description='Django Twisted Extensions - Examples',
    author='Alexander Zykov',
    author_email='tigernwh@gmail.com',
    url='https://github.com/TigerND/dtx-examples',
    install_requires = [
        'Django>=1.5.1',
        'dtx-core>=0.9.3',
        'gittip-twisted>=0.1.1',
        'pyOpenSSL'
    ],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
