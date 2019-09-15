from big_fiubrother_core.message_clients.kafka import Producer
from big_fiubrother_core.messages import VideoChunkMessage
from big_fiubrother_core import StoppableThread


class VideoChunkMessageProducer(StoppableThread):

    def __init__(self, settings, queue):
        self.settings = settings
        self.queue = queue

    def _init(self):
        self.producer = Producer(settings['message_client'])

    def _execute(self):
        camera_output = self.queue.get()
        camera_output['buffer'].seek(0)

        timestamp = datetime.now().strftime('%d-%m-%Y||%H:%M:%S.%f')

        message = VidedChunkMessage(camera_output['id'],
                                    camera_output['buffer'].read(),
                                    timestamp)

        self.producer.produce(message)

    def _stop(self):
        self.producer.flush()