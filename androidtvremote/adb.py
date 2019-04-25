import subprocess
import os
import shlex


def exec_cmd(cmd):
    """Execute the command."""
    # print(shlex.split(cmd))
    try:
        output = subprocess.check_output(shlex.split(cmd))
        return output.decode("utf-8").strip()
    except Exception as e:
        print(str(e))
        # raise


class ADB:
    """Limited set of ADB commands."""

    serial = None

    def __init__(self):
        self.adb_path = exec_cmd("which adb")
        if not self.adb_path:
            raise RuntimeError(
                "You need Android Platform Tools installed and available on your PATH. https://developer.android.com/studio/releases/platform-tools#download"
            )

    def cmd(self, cmd):
        """Run adb command."""
        parts = [self.adb_path]
        if self.serial:
            parts.append("-s %s" % self.serial)
        parts.append(cmd)
        return " ".join(parts)

    def check_connection(self, ip):
        """Check if we have device with the IP."""
        cmd = self.cmd("devices")
        if ip in exec_cmd(cmd):
            # if ip in str(subprocess.check_output(['adb', 'devices'])):
            print(f"Found device with IP {ip}")
            return True
        print("Found no devices")
        return False

    def connect(self, ip, err_count=0):
        """Connect to the device via ADB connect."""
        cmd = self.cmd(f"connect {ip}")
        if "unable" in exec_cmd(cmd):
            # if "unable" in str(subprocess.check_output(['adb', 'connect', ip])):
            err_count += 1
            if err_count >= 3:
                print(f"Unable to connect to {ip} after {err_count} retries")
                return False
            else:
                return connect(ip, err_count)
        print(f"Connected to {ip}")
        # self.serial = self.get_serialno()
        # print(self.serial)
        return True

    def is_connected(self, ip):
        """Determine if device is connected."""
        # By checking if we can get the serial, we can determine
        # if a device is connected.
        return self.get_serialno()

    # General Commands -------------------------------------------------------

    def devices(self, descriptions=True):
        """Print a list of all devices. Use the -l option to
        include the device descriptions."""
        cmd = ["devices"]
        if descriptions:
            cmd.append("-l")
        cmd = " ".join(cmd)

        cmd = self.cmd(cmd)
        return exec_cmd(cmd)

    # File Transfer Commands --------------------------------------------------

    def push(self, local, remote="/data/local/tmp/"):
        """Copy files and directories from the local device (computer) to
        a remote location on the device."""
        cmd = self.cmd(
            "push {local} {remote}".format(
                local=os.path.expanduser(local), remote=remote
            )
        )
        return exec_cmd(cmd)

    def pull(self, remote, local, preserve_meta=False):
        """Copy remote files and directories to a device. Use the -a option
        to preserve the file time stamp and mode."""
        # cmd = self.cmd('pull {remote} {local}'.format(
        #     local=os.path.expanduser(local),
        #     remote=remote
        # ))
        # return exec_cmd(cmd)
        raise NotImplementedError

    # App Installation Commands -----------------------------------------------

    def install(self, apk_file):
        """Install app."""
        cmd = self.cmd(f"install -r {apk_file}")
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
        """Print the adb state of a device. The adb state can be print
        offline, bootloader, or device."""
        cmd = self.cmd("get-state")
        return exec_cmd(cmd)

    def get_serialno(self):
        """"Print the adb device serial number string."""
        if self.serial:
            return self.serial

        cmd = self.cmd("get-serialno")
        return exec_cmd(cmd)

    def get_devpath(self):
        """Print the adb device path."""
        cmd = self.cmd("get-devpath")
        return exec_cmd(cmd)

    def remount(self):
        """Remount the /system, /vendor, and /oem partitions in
        read-write mode."""
        raise NotImplementedError

    def reboot(self, mode=""):
        """Reboot the device [bootloader | recovery | sideload | sideload-auto-reboot]."""
        cmd = self.cmd(f"reboot {mode}")
        return exec_cmd(cmd)

    # Misc --------------------------------------------------------------------

    def set_home_activity(self, package, activity):
        """Set home activity."""
        cmd = self.cmd(
            "shell cmd package set-home-activity {package}/{activity}".format(
                package=package, activity=activity
            )
        )
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
        cmd.append("{package}/{activity}".format(package=package, activity=activity))
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

    def max_volume(self):
        """Set max volume. NOTE: Use with care. Fragile! The interface
        may change in future versions of Android!"""
        # https://github.com/aosp-mirror/platform_frameworks_base/blob/nougat-release/media/java/android/media/IAudioService.aidl
        # 3 = IAudioService method #3 "setStreamVolume"
        # 3 = STREAM_MUSIC constant
        # 15 = max volume (0 - 15)
        cmd = self.cmd("shell service call audio 3 i32 3 i32 15")
        return exec_cmd(cmd)

    def get_ip_address(self):
        """Extract IP address from ifconfig."""
        cmd = self.cmd("shell ifconfig wlan0")
        status, stdout, stderr = exec_cmd(cmd)
        if status and stdout:
            match_obj = re.search(r"inet addr:(.+)  Bcast", stdout, re.M | re.I)
            if match_obj:
                return match_obj.group(1)
        return "N/A"

    # Other -------------------------------------------------------------------

    def reset(self):
        """Reset."""
        self.serial = None
