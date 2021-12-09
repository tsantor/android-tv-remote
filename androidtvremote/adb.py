# -*- coding: utf-8 -*-

import logging
import os
import re
import shlex
import subprocess
import sys

logger = logging.getLogger(__name__)


def exec_cmd(cmd):
    """Execute the command and return clean output"""
    # logger.debug(cmd)
    cmd = shlex.split(cmd, posix="win" not in sys.platform)
    output = subprocess.check_output(cmd)
    return output.decode("utf-8").strip()


class ADB:
    """
    Limited set of ADB commands.
    https://developer.android.com/studio/command-line/adb
    """

    serial = None
    ip = None

    def __init__(self):
        if sys.platform == "win32":
            self.adb_path = exec_cmd("where adb")
        else:
            self.adb_path = exec_cmd("which adb")

        logging.debug(self.adb_path)

        if not self.adb_path:
            raise RuntimeError(
                "You need Android Platform Tools installed and available on your PATH. https://developer.android.com/studio/releases/platform-tools#download"
            )

    def __str__(self):
        return self.serial or self.ip or "Unknown Device"

    def cmd(self, cmd):
        """Return adb command string."""
        parts = [self.adb_path]
        if self.serial:
            parts.append(f"-s {self.serial}")
        parts.append(cmd)
        return " ".join(parts)

    def tcp(self):
        cmd = self.cmd("tcpip 5555")
        return exec_cmd(cmd)

    # General Commands -------------------------------------------------------

    def devices(self, descriptions=True):
        """Print a list of all devices. Use the -l option to
        include the device descriptions."""
        cmd = [f"{self.adb_path} devices"]
        if descriptions:
            cmd.append("-l")
        cmd = " ".join(cmd)
        return exec_cmd(cmd)

    # Connectivity -----------------------------------------------------------

    def check_connection(self, ip):
        """Check if we have device with the IP."""
        cmd = f"{self.adb_path} devices"
        if ip in exec_cmd(cmd):
            logger.info(f"Found device with IP {ip}")
            return True
        logger.warning("Found no devices")
        return False

    def connect(self, ip, err_count=0):
        """Connect to the device via ADB connect."""
        cmd = f"{self.adb_path} connect {ip}"
        if "failed" in exec_cmd(cmd):
            err_count += 1
            if err_count >= 3:
                logger.error(f"Unable to connect to {ip} after {err_count} retries")
                raise RuntimeError(
                    f"Unable to connect to {ip} after {err_count} retries"
                )
            else:
                return self.connect(ip, err_count)
        self.ip = ip
        logger.info(f"Connected to {ip}")
        return True

    def is_connected(self):
        """Determine if device is connected."""
        raise NotImplementedError

    def disconnect(self):
        """Disconnect device."""
        cmd = self.cmd(f"disconnect")
        return exec_cmd(cmd)


    # File Transfer Commands --------------------------------------------------

    def push(self, local, remote="/data/local/tmp/"):
        """Copy files and directories from the local device (computer) to
        a remote location on the device."""
        cmd = self.cmd(f"push {local} {remote}")
        return exec_cmd(cmd)

    def pull(self, remote, local, preserve_meta=False):
        """Copy remote files and directories to a device. Use the -a option
        to preserve the file time stamp and mode."""
        cmd = ["pull"]
        if preserve_meta:
            cmd.append("-k")
        cmd.append(f"{remote} {local}")
        cmd = " ".join(cmd)
        cmd = self.cmd(cmd)
        return exec_cmd(cmd)

    # App Installation Commands -----------------------------------------------

    def install(self, apk_file, replace=True):
        """Install app."""
        cmd = ["install"]
        if replace:
            cmd.append("-r")
        cmd.append(apk_file)
        cmd = " ".join(cmd)
        cmd = self.cmd(cmd)
        return exec_cmd(cmd)

    def uninstall(self, package, keep_data=False):
        """Remove this app package from the device. Add the -k option to
        keep the data and cache directories."""
        cmd = ["uninstall"]
        if keep_data:
            cmd.append("-k")
        cmd.append(package)
        cmd = " ".join(cmd)
        cmd = self.cmd(cmd)
        return exec_cmd(cmd)

    # Scripting Commands ------------------------------------------------------

    def get_state(self):
        """Print the adb state of a device. The state can be offline,
        device or no device."""
        cmd = self.cmd("get-state")
        return exec_cmd(cmd)

    def get_serialno(self):
        """"Print the adb device serial number string."""
        if self.serial:
            return self.serial
        cmd = self.cmd("get-serialno")
        serial = exec_cmd(cmd)
        self.serial = serial
        return serial

    def get_devpath(self):
        """Print the adb device path."""
        cmd = self.cmd("get-devpath")
        return exec_cmd(cmd)

    def remount(self):
        """Remount the /system, /vendor, and /oem partitions in
        read-write mode."""
        raise NotImplementedError

    def reboot(self, mode=None):
        """Reboot the device [bootloader | recovery | sideload | sideload-auto-reboot]."""
        cmd = ["reboot"]
        if mode:
            cmd.append(mode)
        cmd = " ".join(cmd)
        cmd = self.cmd(cmd)
        return exec_cmd(cmd)

    # Misc --------------------------------------------------------------------

    def set_home_activity(self, package, activity):
        """Set home activity."""
        cmd = self.cmd(f"shell cmd package set-home-activity {package}/{activity}")
        return exec_cmd(cmd)

    def start_app(self, package, activity, wait=True, stop=True):
        """Start app."""
        cmd = ["shell am start"]
        # wait for launch to complete
        if wait:
            cmd.append("-W")
        # force stop the target app before starting the activity
        if stop:
            cmd.append("-S")
        cmd.append(f"{package}/{activity}")
        cmd = " ".join(cmd)
        cmd = self.cmd(cmd)
        return exec_cmd(cmd)

    def stop_app(self, package):
        """Force stop everything associated with <PACKAGE>."""
        cmd = self.cmd(f"shell am force-stop {package}")
        return exec_cmd(cmd)

    def list_3rd_party_packages(self):
        """List 3rd party packages."""
        cmd = self.cmd("shell cmd package list packages -3")
        return exec_cmd(cmd)

    def kill_all(self):
        """Kill all background processes."""
        cmd = self.cmd("shell am kill-all")
        return exec_cmd(cmd)

    def stop_service(self, service):
        """Stop a service."""
        cmd = self.cmd(f"shell am stopservice {service}")
        return exec_cmd(cmd)

    def input_keyevent(self, keycode):
        """Send keyevent."""
        cmd = self.cmd(f"shell input keyevent {keycode}")
        return exec_cmd(cmd)

    def get_ip_address(self, interface="wlan0"):
        """Extract IP address from ifconfig."""
        cmd = self.cmd(f"shell ifconfig {interface}")
        result = exec_cmd(cmd)
        if result:
            match_obj = re.search(r"inet addr:(.+)  Bcast", result, re.M | re.I)
            if match_obj:
                return match_obj.group(1)
        return "N/A"

    # Other -------------------------------------------------------------------

    def reset(self):
        """Reset."""
        logger.debug("RESET")
        self.serial = None
        self.ip = None
