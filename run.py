#!/usr/bin/python3

import yaml
from big_fiubrother_camera.helper import configure_logger
from big_fiubrother_camera.mqtt_wrapper import MqttWrapper
from big_fiubrother_camera.image_processor import ImageProcessor
from big_fiubrother_camera.camera_factory import CameraFactory

if __name__ == "__main__":
    print('[*] Configuring big-fiubrother-camera')

    with open('config.yml') as config_file:    
        settings = yaml.load(config_file)

    configure_logger(settings['logger'])

    message_client = MqttWrapper(settings['message_client'])

    image_processor = ImageProcessor(message_client, settings['location'])

    camera = CameraFactory.build(settings['camera']['type'], 
                                 settings['camera']['options'])

    print('[*] Configuration finished. Starting to send frames')
    
    camera.start(image_processor)

    # Stops when image processor receives signal
    print('[*] Stopping camera')
    
    image_processor.close()
    camera.close()