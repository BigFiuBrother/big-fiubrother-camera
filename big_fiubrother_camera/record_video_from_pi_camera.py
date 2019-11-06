from picamera import PiCamera
from big_fiubrother_core import Task
from io import BytesIO


class RecordVideoFromPiCamera(Task):

    def __init__(self, configuration, output_queue):
        self.output_queue = output_queue
        self.recording_time = configuration['recording_time']
        self.resolution = configuration['resolution']
        self.framerate = configuration['framerate']

    def init(self):
        self.camera = PiCamera(resolution=self.resolution,
                               framerate=self.framerate)

    def execute(self):
        buffer = BytesIO()

        # Quality should be between 20 and 25 according to documentation
        self.camera.start_recording(buffer, format='h264', quality=25)
        self.camera.wait_recording(self.recording_time)
        self.camera.stop_recording()

        self.queue.put(buffer)

    def close(self):
        self.camera.close()
