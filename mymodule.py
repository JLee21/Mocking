#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path

# from base_class import Base

def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)

def mock_func(xx):
    return xx

def mock_func_that_uses_other_func():
    xx = 2
    yy = mock_func(xx)
    return yy

class MyClass():

    def class_mock_one(self):
        return 1

    def class_mock_two(self):
        return self.class_mock_one()

class Base():
    def __init__(self):
        self.attr = 'original_value'

    def show(self):
        print('\nBase show:', self.attr)

class Base2():
    global attr
    attr = '\noriginal_value'

    @staticmethod
    def show():
        print(attr)

class App():
    """ Inherit a class from base_class.py. """
    base = Base()
