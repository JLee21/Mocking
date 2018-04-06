#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

import os.path
import tempfile
import unittest

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
from mymodule import rm, mock_func

import mock
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

@mock.patch('mymodule')
def test_mock_func(mock_mod):
    mock_mod.mock_func.return_value = 1

    mock_func(2)
