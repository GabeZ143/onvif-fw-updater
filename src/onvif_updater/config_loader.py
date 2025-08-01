import yaml
from .client import OnvifClient

def load_config(path: str):
    """
    Expects config.yaml to define:
    cameras:
      - host: 192.168.1.10
        port: 30001
        user: admin
        pass: password
    firmware_url: http://zima:8000/firmware.bin
    """
    with open(path) as f:
        data = yaml.safe_load(f)
    cams = []
    for c in data['cameras']:
        cams.append(OnvifClient(
            host=c['host'],
            port=c.get('port', 80),
            user=c['user'],
            password=c['pass'],
            wsdl_dir=data.get('wsdl_dir')
        ))
    return cams, data['firmware_url']
