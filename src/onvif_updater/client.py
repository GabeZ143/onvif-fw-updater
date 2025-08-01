from onvif import ONVIFCamera
from zeep.wsse.username import UsernameToken

class OnvifClient:
    def __init__(self, host, port, user, password, wsdl_dir=None, wsdl_cache=True):
        """
        host: camera IP or hostname
        port: ONVIF (control) port—e.g. 30001
        user/pass: ONVIF credentials
        wsdl_dir: path to local copy of ONVIF WSDLs (optional)
        """
        self.user     = user
        self.password = password

        # Create the camera wrapper
        self.cam = ONVIFCamera(
            host, port, user, password,
            wsdl_dir=wsdl_dir,
            wsdl_cache=wsdl_cache
        )
        # Create the Device Management service proxy
        self.devicemgmt = self.cam.create_devicemgmt_service()
        # Attach a WS-Security UsernameToken (if needed)
        self.devicemgmt._client.wsse.append(UsernameToken(user, password))

    def upgrade_firmware(self, firmware_url: str):
        """
        Triggers UpgradeSystemFirmware over ONVIF.
        """
        body = {
            'Firmware': {
                'Uri': firmware_url
            }
        }
        # This will send the correct SOAP envelope with WS-Security headers
        return self.devicemgmt.UpgradeSystemFirmware(body)

    def get_device_info(self):
        """
        Example helper: calls GetDeviceInformation
        """
        return self.devicemgmt.GetDeviceInformation()
