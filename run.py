#!/usr/bin/env python3

from queue import Queue
from big_fiubrother_camera import (
    BuildVideoChunkMessage,
    RecordVideoFromPiCamera
)
from big_fiubrother_core import (
    SignalHandler,
    StoppableThread,
    PublishToRabbitMQ,
    setup
)


if __name__ == "__main__":
    configuration = setup('Big Fiubrother Camera Application')

    print('[*] Configuring big-fiubrother-camera')

    recorder_to_builder_queue = Queue()
    builder_to_publisher_queue = Queue()

    recorder = StoppableThread(
        RecordVideoFromPiCamera(configuration=configuration['video_recorder'],
                                output_queue=recorder_to_builder_queue))

    message_builder = StoppableThread(
        BuildVideoChunkMessage(configuration=configuration['camera'],
                               input_queue=recorder_to_builder_queue,
                               output_queue=builder_to_publisher_queue))

    publisher = StoppableThread(
        PublishToRabbitMQ(
            configuration=configuration['publisher'],
            input_queue=builder_to_publisher_queue))

    signal_handler = SignalHandler(callback=recorder.stop)

    print('[*] Configuration finished. Starting big-fiubrother-camera!')

    publisher.start()
    message_builder.start()
    recorder.run()

    # STOP Signal received!
    message_builder.stop()
    publisher.stop()
    message_builder.wait()
    publisher.wait()

    print('[*] big-fiubrother-camera stopped!')
