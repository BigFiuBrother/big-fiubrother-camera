from io import IOBytes
import cv2

class VideoCamera:

  def  __init__(self, settings):
    super().__init__()
    self.camera = cv2.VideoCapture(0)

  def start(self, image_processor):
    image = IOBytes()

    stop_capturing = False 
    
    while not stop_capturing:
      success, frame = cap.read()

      if success:
        image = cv2.imencode('.jpeg', frame).tobytes()
        stop_capturing = image_processor.process(image)
        image.truncate()
        image.seek(0)

  def close(self):
    self.camera.release()