#!/usr/bin/env python

import sys
from setuptools import setup

with open('version.txt') as f:
    version_name = f.read().strip()

install_requires = [
    'pandas>=0.19.2',
]

setup(
    name='tabutil',
    url='https://github.com/usf-hii/tabutil',
    version=version_name,
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
