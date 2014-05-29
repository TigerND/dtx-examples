#!/usr/bin/env python

from setuptools import setup

setup(
    name='dtx-examples',
    version='0.9.1',
    description='Gittip APIs Example',
    author='Alexander Zykov',
    author_email='tigernwh@gmail.com',
    url='https://github.com/TigerND/dtx-examples',
    install_requires = [
        'Django>=1.5.1',
        'dtx-core>=0.9.1',
        'gittip-twisted>=0.1.1',
    ],
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)
