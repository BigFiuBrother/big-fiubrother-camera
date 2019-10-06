from big_fiubrother_core.message_clients.rabbitmq import Publisher
from big_fiubrother_core.messages import VideoChunkMessage
from big_fiubrother_core import StoppableThread
import datetime


class VideoChunkMessagePublisher(StoppableThread):

    def __init__(self, publisher_configuration, queue):
        super().__init__()
        self.publisher_configuration = publisher_configuration
        self.queue = queue

    def _init(self):
        self.publisher = Publisher(self.publisher_configuration)

    def _execute(self):
        print('Waiting for message')
        camera_output = self.queue.get()
        print('Messaged received!')
        if camera_output is not None:
            camera_output['buffer'].seek(0)

            timestamp = datetime.now().strftime('%d-%m-%Y||%H:%M:%S.%f')

            message = VidedChunkMessage(camera_output['id'],
                                        camera_output['buffer'].read(),
                                        timestamp)

            self.publisher.publish(message)

    def _stop(self):
        self.queue.put(None)