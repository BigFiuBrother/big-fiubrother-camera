from picamera import PiCamera
from io import BytesIO

class RaspCamera:

    def  __init__(self, settings):
        self.camera = PiCamera(resolution=settings['resolution'],
                               framerate=settings['framerate'])

    def start(self, image_processor):
        image_buffer = BytesIO()

        for foo in self.camera.capture_continuous(image_buffer, format='jpeg'):
            image_buffer.seek(0)
            image = image_buffer.read()

            stop_capturing = image_processor.process(image)
            image_buffer.truncate()
            image_buffer.seek(0)

            if stop_capturing:
                break

    def close(self):
        self.camera.close()