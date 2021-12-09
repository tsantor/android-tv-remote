# -*- coding: utf-8 -*-

import logging
import subprocess

logger = logging.getLogger(__name__)


class AndroidTVRemote:
    """Simple Android TV Remote control."""

    # https://developer.android.com/reference/android/view/KeyEvent.html#KEYCODE_TV_INPUT_HDMI_1
    KEYCODE_HOME = 3
    KEYCODE_BACK = 4

    KEYCODE_DPAD_UP = 19
    KEYCODE_DPAD_DOWN = 20
    KEYCODE_DPAD_LEFT = 21
    KEYCODE_DPAD_RIGHT = 22

    KEYCODE_VOLUME_UP = 24
    KEYCODE_VOLUME_DOWN = 25

    KEYCODE_POWER = 26

    KEYCODE_ENTER = 66

    KEYCODE_VOLUME_MUTE = 164

    KEYCODE_TV_INPUT = 178

    KEYCODE_SOFT_SLEEP = 276
    KEYCODE_SLEEP = 223
    KEYCODE_WAKEUP = 224

    KEYCODE_TV_INPUT_HDMI_1 = 243
    KEYCODE_TV_INPUT_HDMI_2 = 244
    KEYCODE_TV_INPUT_HDMI_3 = 245
    KEYCODE_TV_INPUT_HDMI_4 = 246

    def __init__(self, adb):
        logger.debug(f"Create remote for {adb}")
        self.adb = adb

    # Navigation
    def press_home(self):
        logger.debug("Press Home")
        self.adb.input_keyevent(self.KEYCODE_HOME)

    def press_back(self):
        logger.debug("Press Back")
        self.adb.input_keyevent(self.KEYCODE_BACK)

    def press_dpad_up(self):
        logger.debug("Press Dpad Up")
        self.adb.input_keyevent(self.KEYCODE_DPAD_UP)

    def press_dpad_down(self):
        logger.debug("Press Dpad Down")
        self.adb.input_keyevent(self.KEYCODE_DPAD_DOWN)

    def press_dpad_left(self):
        logger.debug("Press Dpad Left")
        self.adb.input_keyevent(self.KEYCODE_DPAD_LEFT)

    def press_dpad_right(self):
        logger.debug("Press Dpad Right")
        self.adb.input_keyevent(self.KEYCODE_DPAD_RIGHT)

    def press_enter(self):
        logger.debug("Press Enter")
        self.adb.input_keyevent(self.KEYCODE_ENTER)

    # Volume
    def press_volume_up(self):
        logger.debug("Press Volume Up")
        self.adb.input_keyevent(self.KEYCODE_VOLUME_UP)

    def press_volume_down(self):
        logger.debug("Press Volume Down")
        self.adb.input_keyevent(self.KEYCODE_VOLUME_DOWN)

    def press_volume_mute(self):
        logger.debug("Press Volume Mute")
        self.adb.input_keyevent(self.KEYCODE_VOLUME_MUTE)

    # Sleep / Wake
    def press_power(self):
        logger.debug("Press Power")
        self.adb.input_keyevent(self.KEYCODE_POWER)

    def press_soft_sleep(self):
        logger.debug("Press Soft Sleep")
        self.adb.input_keyevent(self.KEYCODE_SOFT_SLEEP)

    def press_sleep(self):
        logger.debug("Press Sleep")
        self.adb.input_keyevent(self.KEYCODE_SLEEP)

    def press_wakeup(self):
        logger.debug("Press Wakeup")
        self.adb.input_keyevent(self.KEYCODE_WAKEUP)

    # Input
    def press_tv_input(self):
        logger.debug("Press TV input")
        self.adb.input_keyevent(self.KEYCODE_TV_INPUT)

    def press_tv_input_hdmi1(self):
        logger.debug("Press TV input HDMI 1")
        self.adb.input_keyevent(self.KEYCODE_TV_INPUT_HDMI_1)

    def press_tv_input_hdmi2(self):
        logger.debug("Press TV input HDMI 1")
        self.adb.input_keyevent(self.KEYCODE_TV_INPUT_HDMI_2)

    def press_tv_input_hdmi3(self):
        logger.debug("Press TV input HDMI 1")
        self.adb.input_keyevent(self.KEYCODE_TV_INPUT_HDMI_3)

    def press_tv_input_hdmi4(self):
        logger.debug("Press TV input HDMI 1")
        self.adb.input_keyevent(self.KEYCODE_TV_INPUT_HDMI_4)
