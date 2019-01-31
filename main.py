#!/usr/bin/python3

import yaml
from modules.helper import configure_logger
from modules.mqtt_wrapper import MqttWrapper
from modules.camera_factory import CameraFactory

if __name__ == "__main__":
    print('Configuring big-fiubrother-camera')

    with open('config.yml') as config_file:    
        settings = yaml.load(config_file)

    configure_logger(settings['logger'])

    message_client = MqttWrapper(settings['message_client'])

    image_processor = ImageProcessor(message_client)

    camera = CameraFactory(settings['camera']['type'], 
                           settings['camera']['options'], 
                           image_processor)

    print('Configuration finished. Starting to send frames')
    
    camera.start()

    # Stops when image processor receives signal
    print('Stopping camera')
    
    image_processor.close()
    camera.close()