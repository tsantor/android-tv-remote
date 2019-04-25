import subprocess
from .adb import ADB


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

    KEYCODE_SLEEP = 223
    KEYCODE_WAKEUP = 224

    KEYCODE_TV_INPUT_HDMI_1 = 243  # Not working on Mi projector
    KEYCODE_TV_INPUT_HDMI_2 = 244  # Not working on Mi projector
    KEYCODE_TV_INPUT_HDMI_3 = 245  # Not working on Mi projector
    KEYCODE_TV_INPUT_HDMI_4 = 246  # Not working on Mi projector

    def __init__(self, ip):
        print(f"Create remote for {ip}")
        self.device_ip = ip
        self.adb = ADB()

    # Navigation
    def press_home(self):
        self.adb.input_keyevent(self.KEYCODE_HOME)

    def press_back(self):
        self.adb.input_keyevent(self.KEYCODE_BACK)

    def press_dpad_up(self):
        self.adb.input_keyevent(self.KEYCODE_DPAD_UP)

    def press_dpad_down(self):
        self.adb.input_keyevent(self.KEYCODE_DPAD_DOWN)

    def press_dpad_left(self):
        self.adb.input_keyevent(self.KEYCODE_DPAD_LEFT)

    def press_dpad_right(self):
        self.adb.input_keyevent(self.KEYCODE_DPAD_RIGHT)

    def press_enter(self):
        self.adb.input_keyevent(self.KEYCODE_ENTER)

    # Volume
    def press_volume_up(self):
        self.adb.input_keyevent(self.KEYCODE_VOLUME_UP)

    def press_volume_down(self):
        self.adb.input_keyevent(self.KEYCODE_VOLUME_DOWN)

    def press_volume_mute(self):
        self.adb.input_keyevent(self.KEYCODE_VOLUME_MUTE)

    # Sleep / Wake
    def press_power(self):
        self.adb.input_keyevent(self.KEYCODE_POWER)

    def press_sleep(self):
        self.adb.input_keyevent(self.KEYCODE_SLEEP)

    def press_wakeup(self):
        self.adb.input_keyevent(self.KEYCODE_WAKEUP)

    # Input
    def press_tv_input(self):
        print("Press TV input")
        self.adb.input_keyevent(self.KEYCODE_TV_INPUT)
