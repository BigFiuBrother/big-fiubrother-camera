from picamera import PiCamera
from io import IOBytes

class RaspCamera:

  def  __init__(self, settings):
    super().__init__()
    self.camera = picamera.PiCamera(resolution=settings.resolution,
                                    framerate=settings.framerate)

  def start(self, image_processor):
    image = IOBytes()

    for foo in self.camera.capture_continous(image, format='jpeg')
      stop_capturing = image_processor.process(image)
      image.truncate()
      image.seek(0)

      if stop_capturing:
        break

  def close(self):
    self.camera.close()