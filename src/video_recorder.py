from picamera import PiCamera
from datetime import datetime
from .local_video import get_filename, create_local_storage, FORMAT


class VideoRecorder:

    def __init__(self, configuration, output_queue):
        self.camera = PiCamera(resolution=configuration['resolution'], framerate=configuration['framerate'])
        self.recording_time = configuration['recording_time']
        self.output_queue = output_queue
        create_local_storage()

    def record(self, is_running):
        timestamp = datetime.now().timestamp()
        self.camera.start_recording(get_filename(timestamp), format=FORMAT, quality=25)

        while is_running():
            self.camera.wait_recording(self.recording_time)
            self.output_queue.put(timestamp)

            timestamp = datetime.now().timestamp()
            self.camera.split_recording(get_filename(timestamp), format=FORMAT, quality=25)

        self.camera.stop_recording()
        self.camera.close()
