import re

import pytest

from androidtvremote import ADB


@pytest.fixture
def serial() -> str:
    return "192.168.1.112"  # Update with your device


@pytest.fixture
def adb(serial) -> ADB:
    adb = ADB()
    # adb.tcp()  # Enable TCP mode to connect over IP
    adb.connect(serial)
    return adb


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
    ip_address = adb.get_ip_address()
    ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
    assert re.match(ip_pattern, ip_address)


def test_devices(adb):
    assert isinstance(adb.devices(), list)


def test_list_3rd_party_packages(adb):
    assert isinstance(adb.list_3rd_party_packages(), list)


def test_list_services(adb):
    assert isinstance(adb.list_services(), list)
