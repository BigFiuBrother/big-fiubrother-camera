
class CameraFactory:

    @staticmethod
    def build(configuration):
        camera_type = configuration['type']

        if camera_type == "picamera":
            from picamera import PiCamera
            return PiCamera(resolution=configuration['resolution'], framerate=configuration['framerate'])

        elif camera_type == "opencv_webcam":
            from big_fiubrother_camera.opencv_webcam import OpenCVWebcam
            return OpenCVWebcam(resolution=configuration['resolution'], framerate=configuration['framerate'])

