#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from setuptools import setup


def find_version(fname):
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version

__version__ = find_version("kkconst/__init__.py")


def read(fname):
    with open(fname) as fp:
        content = fp.read()
    return content


setup(
    name='kkconst',
    version=__version__,
    description='Define const field and const class, customize it as You Like (Python)',
    long_description=read('README.rst'),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
      ],
    keywords=('kkconst', 'const', 'constfield'),
    author='ZHONG KAIXIANG',
    author_email='xiang.ace@gmail.com',
    url='https://github.com/kaka19ace/kkconst/',
    license='http://opensource.org/licenses/MIT',
    packages=['kkconst'],
    include_package_data=True,
    zip_safe=False
)
