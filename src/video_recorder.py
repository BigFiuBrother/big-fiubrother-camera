from picamera import PiCamera
from datetime import datetime
from .video import get_filename, FORMAT


class VideoRecorder:

    def __init__(self, configuration, output_queue):
        self.camera = PiCamera(resolution=configuration['resolution'], framerate=configuration['framerate'])
        self.recording_time = configuration['recording_time']
        self.output_queue = output_queue

    def record(self, is_running):
        now = datetime.now()
        self.camera.start_recording(get_filename(now), format=FORMAT, quality=25)

        while is_running():
            self.camera.wait_recording(self.recording_time)
            self.output_queue.put(now)

            now = datetime.now()
            self.camera.split_recording(get_filename(now), format=FORMAT, quality=25)

        self.camera.stop_recording()
        self.camera.close()
