from big_fiubrother_camera.signal_handler import SignalHandler 
from big_fiubrother_core.camera_message import CameraMessage
from datetime import datetime
import logging
import pickle

class ImageProcessor:

    def __init__(self, message_client):
        self.message_client = message_client
        self.signal_handler = SignalHandler()

    def process(self, camera_id, image):
        timestamp = datetime.now().strftime('%d-%m-%Y||%H:%M:%S.%f')

        message = CameraMessage(camera_id,
                                image,
                                timestamp)

        self.message_client.send(pickle.dumps(message))

        logging.debug('Message sent')

        return self.signal_handler.stop_signal_received

    def close(self):
        self.message_client.close()