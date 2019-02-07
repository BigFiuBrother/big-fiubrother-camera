class CameraFactory:

    @staticmethod
    def build(camera_name, settings):
        normalized_camera_name = camera_name.lower()

        if normalized_camera_name == 'videocamera':
            from big_fiubrother_camera.video_camera import VideoCamera
            return VideoCamera(settings)
        elif normalized_camera_name == 'raspcamera':
            from big_fiubrother_camera.rasp_camera import RaspCamera
            return RaspCamera(settings)
        else:
            raise Exception('Wrong camera type')
