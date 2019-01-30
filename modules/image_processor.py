from modules.signal_handler import SignalHandler 
from datetime import datetime
import base64
import json

class ImageProcessor:

    def __init__(self, message_client, location):
        self.message_client = message_client
        self.signal_handler = SignalHandler()
        self.location = [location['latitude'], location['longitude']]

    def process(image):
        payload = {}

        payload['location'] = config['camera']['location']
        payload['timestamp'] = datetime.now().strftime('%d-%m-%Y||%H:%M:%S.%f')
        payload['frame'] = base64.b64encode(image).decode('utf-8')

        message = json.dumps(payload)

        self.message_client.send(message)

        logging.debug('Message sent: %d'.format(message))

        return signal_handler.stop_signal_received

    def close():
        self.message_client.close()