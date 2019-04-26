#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import re

# target = __import__("adb.py")
from androidtvremote import adb


class TestADB(unittest.TestCase):
    def setUp(self):
        self.adb = adb.ADB()

    def test_is_connected(self):
        self.assertTrue(self.adb.is_connected())

    def test_get_state(self):
        result = self.adb.get_state()
        matches = re.match(r"[\w\s]+", result)
        self.assertEqual(result, matches.group(0))

    def test_get_serialno(self):
        result = self.adb.get_serialno()
        matches = re.match(r"[\w\.\:]+", result)
        self.assertEqual(result, matches.group(0))

    # def test_stop_service(self):
    #     result = self.adb.stop_service('com.android.printspooler')

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
