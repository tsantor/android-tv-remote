import pytest

from androidtvremote.adb import ADB
from androidtvremote.remote import AndroidTVRemote


@pytest.fixture(scope="session")
def serial() -> str:
    return "192.168.1.206"  # Update with your device


@pytest.fixture(scope="session")
def adb(serial) -> ADB:
    adb = ADB()
    adb.connect(serial)
    return adb


@pytest.fixture(scope="session")
def remote(adb) -> AndroidTVRemote:
    return AndroidTVRemote(adb)


def test_press_home(remote):
    remote.press_home()


def test_press_back(remote):
    remote.press_back()


def test_press_dpad_up(remote):
    remote.press_dpad_up()


def test_press_dpad_down(remote):
    remote.press_dpad_down()


def test_press_dpad_left(remote):
    remote.press_dpad_left()


def test_press_dpad_right(remote):
    remote.press_dpad_right()


def test_press_enter(remote):
    remote.press_enter()


def test_press_volume_up(remote):
    remote.press_volume_up()


def test_press_volume_down(remote):
    remote.press_volume_down()


def test_press_volume_mute(remote):
    remote.press_volume_mute()


def test_press_power(remote):
    remote.press_power()


def test_press_soft_sleep(remote):
    remote.press_soft_sleep()


def test_press_sleep(remote):
    remote.press_sleep()


def test_press_wakeup(remote):
    remote.press_wakeup()


def test_press_tv_input(remote):
    remote.press_tv_input()


def test_press_tv_input_hdmi1(remote):
    remote.press_tv_input_hdmi1()


def test_press_tv_input_hdmi2(remote):
    remote.press_tv_input_hdmi2()


def test_press_tv_input_hdmi3(remote):
    remote.press_tv_input_hdmi3()


def test_press_tv_input_hdmi4(remote):
    remote.press_tv_input_hdmi4()
