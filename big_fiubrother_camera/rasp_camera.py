from picamera import PiCamera
from io import BytesIO


class RaspCamera:

    def  __init__(self, id, configuration, queue):
        self.id = id
        self.queue = queue
        self.running = False
        self.recording_time = configuration['recording_time']
        
        self.camera = PiCamera(resolution=configuration['resolution'], framerate=configuration['framerate'])

    def start(self):
        self.running = True

        while self.running:
            buffer = BytesIO()
            
            #Quality should be between 20 and 25 according to documentation
            self.camera.start_recording(buffer, format='h264', quality=21)
            self.camera.wait_recording(self.recording_time)
            self.camera.stop_recording()

            self.queue.put({'id': self.id, 'buffer': buffer})

    def stop(self):
        self.running = False

    def close(self):
        self.camera.close()