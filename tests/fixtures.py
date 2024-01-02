import pytest

from androidtvremote import ADB, AndroidTVRemote


@pytest.fixture
def serial() -> str:
    return "192.168.1.206"  # Update with your device


@pytest.fixture
def adb(serial) -> ADB:
    adb = ADB()
    # adb.tcp()  # Enable TCP mode to connect over IP
    adb.connect(serial)
    return adb


@pytest.fixture
def remote(adb) -> AndroidTVRemote:
    return AndroidTVRemote(adb)
