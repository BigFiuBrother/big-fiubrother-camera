from time import sleep
from io import BytesIO
import cv2


class WebCamera:

  def  __init__(self, id, settings):
    super().__init__()
    self.camera = cv2.VideoCapture(0)
    self.id = id
    self.settings = settings

  def start(self, image_processor):
    image = BytesIO()

    stop_capturing = False 
    sleep_time = 1.0 / self.settings['framerate']

    while not stop_capturing:
      capture_success, frame = self.camera.read()

      if capture_success:
        encoding_success, image = cv2.imencode('.jpeg', frame)

        if encoding_success:
          stop_capturing = image_processor.process(self.id, image.tobytes())

      sleep(sleep_time)

  def close(self):
    self.camera.release()