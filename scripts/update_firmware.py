#!/usr/bin/env python3
"""
update_firmware.py

Usage:
  python scripts/update_firmware.py <CAM_IP> <USERNAME> <PASSWORD> <FIRMWARE_URL>
"""

import sys
from onvif import ONVIFCamera

def main():
    if len(sys.argv) != 5:
        print(__doc__)
        sys.exit(1)

    cam_ip, user, pwd, fw_url = sys.argv[1:]
    print(f"Connecting to camera {cam_ip}…")
    cam = ONVIFCamera(cam_ip, 80, user, pwd)
    devmgmt = cam.create_devicemgmt_service()

    print(f"Triggering firmware upgrade from {fw_url} …")
    # The UpgradeSystemFirmware request takes a dict with “URL”
    devmgmt.UpgradeSystemFirmware({'URL': fw_url})

    print("Upgrade request sent. Camera will download and apply firmware.")

if __name__ == "__main__":
    main()