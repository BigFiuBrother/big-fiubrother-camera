from big_fiubrother_camera.camera_factory import CameraFactory
from big_fiubrother_core import Task
from io import BytesIO


class RecordVideoFromCamera(Task):

    def __init__(self, configuration, output_queue):
        self.running = False
        self.output_queue = output_queue
        self.recording_time = configuration['recording_time']
        self.resolution = configuration['resolution']
        self.framerate = configuration['framerate']
        self.configuration = configuration

    def init(self):
        self.running = True
        self.camera = CameraFactory.build(self.configuration)

    def execute(self):
        while self.running:
            buffer = BytesIO()

            # Quality should be between 20 and 25 according to documentation
            self.camera.start_recording(buffer, format='h264', quality=25)
            self.camera.wait_recording(self.recording_time)
            self.camera.stop_recording()

            self.output_queue.put(buffer)

    def stop(self):
        self.running = False

    def close(self):
        self.camera.close()
