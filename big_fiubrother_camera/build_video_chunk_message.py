from big_fiubrother_core.messages import VideoChunkMessage
from big_fiubrother_core import QueueTask
from datetime import datetime


class BuildVideoChunkMessage(QueueTask):

    def __init__(self, configuration, input_queue, output_queue):
        super().__init__(input_queue)
        self.id = configuration['id']
        self.output_queue = output_queue

    def execute_with(self, buffer):
        buffer.seek(0)

        message = VideoChunkMessage(camera_id=self.id,
                                    timestamp=datetime.now().timestamp(),
                                    payload=buffer.read())

        self.output_queue.put(message)
