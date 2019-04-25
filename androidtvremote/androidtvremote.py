# -*- coding: utf-8 -*-

from . import adb
import remote


def main():
    DEVICE_IP = "192.168.1.190"
    adb = adb.ADB()

    adb.check_connection(DEVICE_IP)
    adb.connect(DEVICE_IP)
    serial = adb.get_serialno()
    print(serial)
    devices = adb.devices()
    print(devices)

    remote = remote.AndroidTVRemote(DEVICE_IP)
    remote.press_tv_input()


if __name__ == "__main__":
    main()
