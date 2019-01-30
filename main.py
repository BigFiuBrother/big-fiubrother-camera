#!/usr/bin/python3

import yaml
from modules.graceful_killer import GracefulKiller
from modules.logger import configure_logger
from modules.mqtt_wrapper import MqttWrapper
from datetime import datetime
from time import sleep
import base64

if __name__ == "__main__":
    print('Configuring big-fiubrother-camera')

    with open('config.yml') as config_file:    
        settings = yaml.load(config_file)

    configure_logger(settings['logger'])

    client = MqttWrapper(settings['message_client'])

    signal_handler = SignalHandler()

  if config['camera']['type'] == "mock": 
    from modules.mock_camera import *
    camera = MockCamera() 
  elif config['camera']['type'] == "pi":
    from modules.rasp_camera import *
    camera = RaspCamera(settings['camera']['options'])

    print('Configuration finished. Starting to send frames')
    
  while not signal_handler.stop_signal_received:  
    payload['location'] = config['camera']['location']
    payload['timestamp'] = datetime.now().strftime('%d-%m-%Y||%H:%M:%S.%f')
    payload['frame'] = camera.get_frame()

    if payload['frame'] != camera.INVALID():
      payload['frame'] = payload['frame'].decode('utf-8')
      
      client.send(config['network']['topic'],json.dumps(payload))

      print('Mensaje de frame enviado')
      logging.debug('Se envió: \'{'+str(payload['location'])+','+payload['timestamp']+'}\'')

    sleep(sleep_time)

    if killer.kill_now:
      break

  print('Se recibió una señal de salida, cerrando conexión')

  client.close()
  camera.close()