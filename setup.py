#!/usr/bin/env python

import sys
from setuptools import setup

install_requires = [
    'pandas>=0.19.2',
]

setup(
    name='tabutil',
    version='0.6.0',
    description='Table Utility with Plink-like functionality',
    author='Kevin Counts',
    author_email='counts@digicat.org',
    license='GPL',
    packages=[
        'tabutil',
    ],
    entry_points={
        'console_scripts': [
            'tabutiln = tabutil.cli:launch_new_instance',
        ]
    },
    install_requires=install_requires
)
