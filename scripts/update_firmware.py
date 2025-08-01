#!/usr/bin/env python3
import sys
from onvif import ONVIFCamera

def main():
    if len(sys.argv) != 5:
        print("Usage: update_firmware.py <CAM_IP> <USER> <PASS> <FW_URL>")
        sys.exit(1)

    cam_ip, user, pwd, fw_url = sys.argv[1:]
    cam = ONVIFCamera(cam_ip, 20001, user, pwd)
    devmgmt = cam.create_devicemgmt_service()

    print(f"Triggering firmware upgrade on {cam_ip}…")
    # pass the entire SOAP body; Zeep will map it to the AttachmentData type
    devmgmt.UpgradeSystemFirmware({ 
        'Firmware': { 
            'Uri': fw_url    # most cameras expect "Uri" here 
        }
    })
    print("Upgrade request sent successfully.")

if __name__ == "__main__":
    main()
