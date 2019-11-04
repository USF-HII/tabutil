#!/usr/bin/env python

import sys
from setuptools import setup

import tabutil

install_requires = [
    'pandas>=0.19.2',
]

setup(
    name='tabutil',
    url='https://github.com/usf-hii/tabutil',
    version=tabutil.__version__,
    description='Table Utility with Plink-like functionality',
    author='Kevin Counts',
    author_email='counts@digicat.org',
    license='GPLv3',
    packages=[
        'tabutil',
    ],
    entry_points={
        'console_scripts': [
            'tabutil = tabutil.cli:main',
        ]
    },
    install_requires=install_requires
)
