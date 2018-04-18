#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm, App, Base, Base2

import os.path
import tempfile
import unittest
import mock
from mock import Mock

"""
Bad way to test.
"""
# class RmTestCase(unittest.TestCase):
#
#     tmpfilepath = os.path.join(tempfile.gettempdir(), "tmp-testfile")
#
#     def setUp(self):
#         with open(self.tmpfilepath, "wb") as f:
#             f.write("Delete me!")
#
#     def test_rm(self):
#         # remove the file
#         rm(self.tmpfilepath)
#         # test that it was actually removed
#         self.assertFalse(os.path.isfile(self.tmpfilepath), "Failed to remove the file.")


"""
Refactor with Mocks
"""
import mymodule
from mymodule import rm, mock_func

import unittest

class RmTestCase(unittest.TestCase):

    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # set up the mock
        mock_path.isfile.return_value = False

        rm("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        rm("any path")

        mock_os.remove.assert_called_with("any path")

@mock.patch('mymodule.mock_func')
def test_mock_func(mock_mod):
    mock_mod.mock_func.return_value = 1
    mock_func(2)

@mock.patch('mymodule.mock_func')
def test_mock_other_func(mock_func):
    """ Call :mock_func_that_uses_other_func: but patch the funcs that it uses.
    """
    mock_func.return_value = 1
    xx = mymodule.mock_func_that_uses_other_func()
    print(xx)

def test_mock_a_class_func():
    """ Call MyClass.class_mock_two(), but mock MyMock.class_mock_one."""
    print()

    myclass = mymodule.MyClass()
    myclass.class_mock_one = Mock()
    myclass.class_mock_one.return_value = 2
    xx = myclass.class_mock_two()
    print(xx)
    myclass.class_mock_one.assert_called_with()

def test_mock_inherited_class_instance_no_mock():
    """ Without mocking. """
    app = App()
    print('\n', app.base.attr)
    assert app.base.attr == 'original_value'

# @mock.patch('mymodule.Base')
def test_mock_inherited_class_instance():
    """ With mocking. Change app.base.attr from 'original_value' to 'new_value'.
    """
    app = App()
    app.base.show()

    app.base = Mock()
    app.base.attr.return_value = 'new'
    app.base.show()

def test_base2():
    Base2.show()
    base2 = Base2()
    base2.show()
