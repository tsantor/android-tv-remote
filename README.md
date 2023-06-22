# Python Android TV Remote
Author:Tim Santor <tsantor@xstudios.com>

## Overview
Simple package that allows you to mimic Android TV remote inputs via Python.  Designed to be used over TCP (not USB).


## Features
Offers a limited set of ADB commands. See [Usage](#Usage) below. Also view `src\androidtvremote\adb.py` for all commands and their params until I create docs.


## Installation
To install python-android-tv-remote, simply:

    pip install android-tv-remote

## Usage

```
from androidtvremote import ADB
from androidtvremote.remote import AndroidTVRemote

IP = '192.168.1.x'

adb = ADB()
adb.connect(IP)
adb.is_connected()
adb.check_connection(IP)
adb.get_state()
adb.get_serialno()
adb.start_app("com.android.chrome", "com.google.android.apps.chrome.Main")
adb.stop_app("com.android.chrome")
adb.input_keyevent("KEYCODE_HOME")
adb.get_ip_address()
adb.devices()
adb.list_3rd_party_packages()
adb.list_services()
adb.disconnect()
adb.kill_server()
adb.start_server()

remote = AndroidTVRemote(adb)
remote.press_home()
remote.press_back()
remote.press_dpad_up()
remote.press_dpad_down()
remote.press_dpad_left()
remote.press_dpad_right()
remote.press_enter()
remote.press_volume_up()
remote.press_volume_down()
remote.press_volume_mute()
remote.press_power()
remote.press_soft_sleep()
remote.press_wakeup()
remote.press_tv_input()
remote.press_tv_input_hdmi1()
remote.press_tv_input_hdmi2()
remote.press_tv_input_hdmi3()
remote.press_tv_input_hdmi4()
```

## Development

    make env
    make reqs
    pip install -e .

## Testing
Project is at **76%** test coverage.

    pytest -v
    tox

    # Run a specific test
    pytest -v tests/test_adb.py -k test_get_ip_address

    # Run coverage
    pytest --cov-report html --cov-report term --cov=tests/


## Documentation
Documentation is available at TODO


## Issues
If you experience any issues, please create an [issue](https://bitbucket.org/tsantor/python-android-tv-remote/issues) on Bitbucket.


## Tips
Get IP address:
```
adb devices
adb -s <DEVICE_ID> shell ip -f inet addr show wlan0
```
