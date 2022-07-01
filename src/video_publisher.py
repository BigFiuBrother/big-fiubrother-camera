from .local_video import get_filename, delete_video
from big_fiubrother_core_events.message_clients.rabbitmq import Publisher
from big_fiubrother_core_events.messages.marshalling import encode_message
from big_fiubrother_core_events.messages.video_chunk_message import VideoChunkMessage
from big_fiubrother_core_video_storage import get_raw_storage

ID_KEY = 'id'
PUBLISHER_KEY = 'publisher'
STORAGE_KEY = 'storage'


class VideoPublisher:

    def __init__(self, input_queue, configuration):
        self.input_queue = input_queue
        self.camera_id = configuration[ID_KEY]
        self.publisher = Publisher(configuration[PUBLISHER_KEY])
        self.storage = get_raw_storage(configuration[STORAGE_KEY])

    def publish(self, is_running):
        while is_running():
            self.input_queue.get(self._publish)

    def _publish(self, timestamp):
        message = VideoChunkMessage(self.camera_id, timestamp)

        # Store video chunk in the cloud
        self.storage.store_file(message.id(), get_filename(timestamp))

        # Send event of new video chunk
        self.publisher.publish(encode_message(message))

        # Delete local video chunk
        delete_video(timestamp)