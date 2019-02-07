from big_fiubrother_camera.signal_handler import SignalHandler 
from datetime import datetime
import logging
import pickle

class ImageProcessor:

    def __init__(self, message_client, location):
        self.message_client = message_client
        self.signal_handler = SignalHandler()
        self.location = [location['latitude'], location['longitude']]

    def process(self, image):
        payload = {}

        payload['location'] = self.location
        payload['timestamp'] = datetime.now().strftime('%d-%m-%Y||%H:%M:%S.%f')
        payload['frameBytes'] = image
        payload['frameId'] = 'tu vieja'

        self.message_client.send(pickle.dumps(message))

        # logging.debug('Message sent: %d'.format(message))

        return self.signal_handler.stop_signal_received

    def close(self):
        self.message_client.close()