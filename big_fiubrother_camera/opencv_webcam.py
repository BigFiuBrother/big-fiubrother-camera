import cv2
import time
from uuid import uuid4 as uuid
import os

class OpenCVWebcam:

    def __init__(self, resolution, framerate):

        # Video capture
        self.video_capture = cv2.VideoCapture(-1)
        self.resolution = tuple([int(num) for num in resolution.split('x')])
        self.framerate = framerate
        self.temp_file = str(uuid()) + ".avi"
        self.video_writer = None
        self.buf = None

    def start_recording(self, buffer, format, quality):
        self.buf = buffer

        # Esto deberia depender de format, por ahora es fijo
        fourcc = cv2.VideoWriter_fourcc(*'X264')
        self.video_writer = cv2.VideoWriter(self.temp_file, fourcc, self.framerate, self.resolution)

    def wait_recording(self, seconds):

        start_time = time.time()
        # Record from webcam to file
        while self.video_capture.isOpened():
            ok, frame = self.video_capture.read()
            if ok:
                self.video_writer.write(frame)

            elapsed_time = time.time() - start_time

            if elapsed_time >= seconds:
                break

    def stop_recording(self):
        # Load file to buffer
        self.video_writer.release()
        with open(self.temp_file, mode='rb') as file:
            self.buf.write(file.read())
        os.remove(self.temp_file)

    def close(self):
        self.video_capture.release()
        self.video_writer.release()

