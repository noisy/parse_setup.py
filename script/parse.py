#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import setuptools


def setup(*args, **kwargs):
    print '#[OK]'
    print '\n'.join(kwargs.get('install_requires'))

setuptools.setup = setup


def read_setup_py_from_stdin():
    setup_py = ''
    for line in sys.stdin:
        setup_py += line

    return setup_py

try:
    exec read_setup_py_from_stdin()
except Exception as e:
    print str(e)
