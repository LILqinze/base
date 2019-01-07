#!/bin/python

from setuptools import find_packages, setup

setup(
    name='munea_core',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/pwr-graphs/base',
    license='',
    author='Mateusz Gaweł, Grzegorz Suszka',
    author_email='',
    description='',
    install_requires=[
        'networkx',
        'scipy',
        'matplotlib',
        'pyunpack'
    ]
)
