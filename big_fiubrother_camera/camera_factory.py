class CameraFactory:

    @staticmethod
    def build(settings):
        normalized_camera_type = settings['type'].lower()

        if normalized_camera_type == 'videocamera':
            from big_fiubrother_camera.video_camera import VideoCamera
            return VideoCamera(settings['camera_id'], settings['options'])
        elif normalized_camera_type == 'raspcamera':
            from big_fiubrother_camera.rasp_camera import RaspCamera
            return RaspCamera(settings['camera_id'], settings['options'])
        else:
            raise Exception('Wrong camera type')
