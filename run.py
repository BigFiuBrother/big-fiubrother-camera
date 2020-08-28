#!/usr/bin/env python3

from queue import Queue
from big_fiubrother_camera import (
    BuildVideoChunkMessage,
    RecordVideoFromCamera
)
from big_fiubrother_core import (
    SignalHandler,
    StoppableThread,
    PublishToRabbitMQ,
    setup,
    run
)


if __name__ == "__main__":
    configuration = setup('Big Fiubrother Camera Application')

    print('[*] Configuring big-fiubrother-camera')

    recorder_to_builder_queue = Queue()

    recorder = StoppableThread(
        RecordVideoFromCamera(configuration=configuration['video_recorder'],
                                output_queue=recorder_to_builder_queue))
    
    builder_to_publisher_queue = Queue()

    message_builder = StoppableThread(
        BuildVideoChunkMessage(configuration=configuration['camera'],
                               input_queue=recorder_to_builder_queue,
                               output_queue=builder_to_publisher_queue))

    publisher = StoppableThread(
        PublishToRabbitMQ(
            configuration=configuration['publisher'],
            input_queue=builder_to_publisher_queue))

    print('[*] Configuration finished. Starting big-fiubrother-camera!')

    run(processes=[message_builder, publisher],
        main_process=recorder)

    print('[*] big-fiubrother-camera stopped!')
