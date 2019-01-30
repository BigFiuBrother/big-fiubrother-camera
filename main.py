#!/usr/bin/python3

import yaml
from modules.helper import configure_logger
from modules.mqtt_wrapper import MqttWrapper

if __name__ == "__main__":
    print('Configuring big-fiubrother-camera')

    with open('config.yml') as config_file:    
        settings = yaml.load(config_file)

    configure_logger(settings['logger'])

    message_client = MqttWrapper(settings['message_cl|ient'])

    image_processor = ImageProcessor(message_client)

    if config['camera']['type'] == "mock": 
        from modules.mock_camera import *
        camera = MockCamera() 
    elif config['camera']['type'] == "pi":
        from modules.rasp_camera import *
        camera = RaspCamera(settings['camera']['options'], image_processor)

    print('Configuration finished. Starting to send frames')
    
    camera.start()

    # Stops when image processor receives signal
    image_processor.close()
    camera.close()