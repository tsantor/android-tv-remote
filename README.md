# Python Android TV Remote
Author:Tim Santor <tsantor@xstudios.com>

## Overview
Simple package that allows you to mimic Android TV remote inputs via Python.  Designed to be used over TCP (not USB).


## Features
Offers a limited set of ADB commands. See `src\androidtvremote\adb.py` for all commands.

    - `tcp`
    - `devices`
    - `connect`
    - `install`
    - `uninstall`
    - `push`
    - `pull`
    - `get-state`
    - `get-serialno`
    - `get-devpath`
    - `reboot`
    - `start-server`
    - `kill-server`



## Installation
To install python-android-tv-remote, simply:

    pip install android-tv-remote

## Tips
Get IP address:
```
adb devices
adb -s <DEVICE_ID> shell ip -f inet addr show wlan0
```


## Documentation
Documentation is available at TODO


## Issues
If you experience any issues, please create an [issue](https://bitbucket.org/tsantor/python-android-tv-remote/issues) on Bitbucket.
