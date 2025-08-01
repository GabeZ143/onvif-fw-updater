#!/usr/bin/env python3
import sys
from onvif_updater.config_loader import load_config
from onvif_updater.firmware import FirmwareUpdater

def main():
    config_path = sys.argv[1] if len(sys.argv) > 1 else 'config.yaml'
    cameras, fw_url = load_config(config_path)
    updater = FirmwareUpdater(cameras, fw_url)
    updater.run()

if __name__ == '__main__':
    main()
