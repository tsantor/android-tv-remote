import re

import pytest

from androidtvremote.adb import ADB
from androidtvremote.remote import AndroidTVRemote

# import unittest

# class TestADB(unittest.TestCase):
#     def setUp(self):
#         self.adb = ADB()
#         # self.adb.tcp()  # Enable TCP mode to connect over IP
#         serial = "192.168.1.112"  # Update with your device
#         self.adb.connect(serial)

#     def test_is_connected(self):
#         self.assertTrue(self.adb.is_connected())

#     def test_get_state(self):
#         result = self.adb.get_state()
#         matches = re.match(r"[\w\s]+", result)
#         self.assertEqual(result, matches[0])

#     def test_get_serialno(self):
#         result = self.adb.get_serialno()
#         matches = re.match(r"[\w\.\:]+", result)
#         self.assertEqual(result, matches[0])

#     # def test_stop_service(self):
#     #     result = self.adb.stop_service('com.android.printspooler')

#     def tearDown(self):
#         pass

# if __name__ == "__main__":
#     unittest.main()


@pytest.fixture
def serial() -> str:
    return "192.168.1.112"  # Update with your device


@pytest.fixture
def adb(serial) -> ADB:
    adb = ADB()
    # adb.tcp()  # Enable TCP mode to connect over IP
    adb.connect(serial)
    return adb


@pytest.fixture
def remote(adb) -> AndroidTVRemote:
    return AndroidTVRemote(adb)


def test_is_connected(adb):
    assert adb.is_connected()


def test_check_connection(adb, serial):
    assert adb.check_connection(serial)


def test_get_state(adb):
    result = adb.get_state()
    matches = re.match(r"[\w\s]+", result)
    assert result == matches[0]


def test_get_serialno(adb):
    result = adb.get_serialno()
    matches = re.match(r"[\w\.\:]+", result)
    assert result == matches[0]


def test_start_app(adb):
    adb.start_app(
        "com.android.chrome", "com.google.android.apps.chrome.Main", False, False
    )


def test_stop_app(adb):
    adb.stop_app("com.android.chrome")


def test_input_keyevent(adb):
    adb.input_keyevent("KEYCODE_HOME")


def test_get_ip_address(adb, serial):
    assert adb.get_ip_address() == serial


def test_remote(remote):
    remote.press_home()
