import re


def build_web_camera(configuration, queue):
    from big_fiubrother_camera.web_camera import WebCamera
    return WebCamera(configuration['id'], configuration['options'], queue)

def build_rasp_camera(configuration, queue):
    from big_fiubrother_camera.rasp_camera import RaspCamera
    return RaspCamera(configuration['id'], configuration['options'], queue)

BUILDING_MAP = {
    'webcamera': build_web_camera,
    'raspcamera': build_rasp_camera
}

def build_camera_recorder(configuration, queue):
    normalized_camera_type = re.sub('_', '', configuration['type'].lower())

    if normalized_camera_type in BUILDING_MAP:
        BUILDING_MAP[normalized_camera_type](configuration, queue)
    else:
        raise Exception('Invalid camera type')