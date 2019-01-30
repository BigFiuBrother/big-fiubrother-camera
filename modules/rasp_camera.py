#!/bin/python3

from picamera import PiCamera
from io import IOBytes

class RaspCamera:

  def  __init__(self, settings):
    super().__init__()
    self.camera = picamera.PiCamera(resolution=settings.resolution,
                                    framerate=settings.framerate)

  def start(self, process_image):
    output = IOBytes()

    for foo in self.camera.capture(output, format='jpeg')
      stop_capturing = process_image(output)
      output.truncate()
      output.seek(0)

      if stop_capturing:
        break

  def close(self):
    self.camera.close()