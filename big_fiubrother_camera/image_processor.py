from big_fiubrother_camera.signal_handler import SignalHandler 
from datetime import datetime
import logging
import base64
import json

class ImageProcessor:

    def __init__(self, message_client, location):
        self.message_client = message_client
        self.signal_handler = SignalHandler()
        self.location = [location['latitude'], location['longitude']]

    def process(self, image):
        payload = {}

        payload['location'] = self.location
        payload['timestamp'] = datetime.now().strftime('%d-%m-%Y||%H:%M:%S.%f')
        payload['frame_bytes'] = base64.b64encode(image).decode('utf-8')
        payload['frame_id'] = 'tu vieja'

        message = json.dumps(payload)

        self.message_client.send(message)

        logging.debug('Message sent: %d'.format(message))

        return self.signal_handler.stop_signal_received

    def close(self):
        self.message_client.close()