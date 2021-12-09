# -*- coding: utf-8 -*-

import logging
import subprocess

logger = logging.getLogger(__name__)


class AndroidTVRemote:
    """Simple Android TV Remote control."""

    # https://developer.android.com/reference/android/view/KeyEvent

    def __init__(self, adb):
        logger.debug(f"Create remote for {adb}")
        self.adb = adb

    # Navigation
    def press_home(self):
        self.adb.input_keyevent("KEYCODE_HOME")

    def press_back(self):
        self.adb.input_keyevent("KEYCODE_BACK")

    def press_dpad_up(self):
        self.adb.input_keyevent("KEYCODE_DPAD_UP")

    def press_dpad_down(self):
        self.adb.input_keyevent("KEYCODE_DPAD_DOWN")

    def press_dpad_left(self):
        self.adb.input_keyevent("KEYCODE_DPAD_LEFT")

    def press_dpad_right(self):
        self.adb.input_keyevent("KEYCODE_DPAD_RIGHT")

    def press_enter(self):
        self.adb.input_keyevent("KEYCODE_ENTER")

    # Volume
    def press_volume_up(self):
        self.adb.input_keyevent("KEYCODE_VOLUME_UP")

    def press_volume_down(self):
        self.adb.input_keyevent("KEYCODE_VOLUME_DOWN")

    def press_volume_mute(self):
        self.adb.input_keyevent("KEYCODE_VOLUME_MUTE")

    # Sleep / Wake
    def press_power(self):
        self.adb.input_keyevent("KEYCODE_POWER")

    def press_soft_sleep(self):
        self.adb.input_keyevent("KEYCODE_SOFT_SLEEP")

    def press_sleep(self):
        self.adb.input_keyevent("KEYCODE_SLEEP")

    def press_wakeup(self):
        self.adb.input_keyevent("KEYCODE_WAKEUP")

    # Input
    def press_tv_input(self):
        self.adb.input_keyevent("KEYCODE_TV_INPUT")

    def press_tv_input_hdmi1(self):
        self.adb.input_keyevent("KEYCODE_TV_INPUT_HDMI_1")

    def press_tv_input_hdmi2(self):
        self.adb.input_keyevent("KEYCODE_TV_INPUT_HDMI_2")

    def press_tv_input_hdmi3(self):
        self.adb.input_keyevent("KEYCODE_TV_INPUT_HDMI_3")

    def press_tv_input_hdmi4(self):
        self.adb.input_keyevent("KEYCODE_TV_INPUT_HDMI_4")
