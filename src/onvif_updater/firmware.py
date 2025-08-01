from typing import List
from .client import OnvifClient

class FirmwareUpdater:
    def __init__(self, cameras: List[OnvifClient], firmware_url: str):
        self.cameras      = cameras
        self.firmware_url = firmware_url

    def run(self):
        for cam in self.cameras:
            print(f"Upgrading {cam.cam.host} → {self.firmware_url}")
            try:
                resp = cam.upgrade_firmware(self.firmware_url)
                print("  Success:", resp)
            except Exception as e:
                print("  Failed:", e)
