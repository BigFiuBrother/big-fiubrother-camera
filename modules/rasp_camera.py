from picamera import PiCamera
from io import BytesIO

class RaspCamera:

    def  __init__(self, settings):
        super().__init__()
        self.camera = PiCamera(resolution=settings['resolution'],
                               framerate=settings['framerate'])

    def start(self, image_processor):
        image = BytesIO()

        for foo in self.camera.capture_continuous(image, format='jpeg'):
            stop_capturing = image_processor.process(image.read())
            image.truncate()
            image.seek(0)

            if stop_capturing:
                break

    def close(self):
        self.camera.close()