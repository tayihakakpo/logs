#!/usr/bin/env python
# encoding: utf-8


from setuptools import setup

import logs


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name="logs",
    author="Thomas Ayih-Akakpo",
    author_email="thomas.ayihakakpo@gmail.com",
    version=logs.__version__,
    py_modules=['logs'],
    description="Log simpler",
    long_description=readme(),
    license='MIT',
    include_package_data=True,
    url='https://github.com/tayihakakpo/logs.git',
)

