from modules.rasp_camera import RaspCamera
from modules.video_camera import VideoCamera


class CameraFactory:

    VIDEO_CAMERA = 'VideoCamera'.lower()
    RASP_CAMERA = 'RaspCamera'.lower()

    @staticmethod
	def build(camera_name, settings, image_processor):
        normalized_camera_name = camera_name.lower()

        if normalized_camera_name == self.VIDEO_CAMERA:
            return VideoCamera(settings, image_processor)
        elif normalized_camera_name == self.RASP_CAMERA:
            return RaspCamera(settings, image_processor)
        else:
            raise Exception('Wrong camera type')
