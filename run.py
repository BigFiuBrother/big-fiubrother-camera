#!/usr/bin/env python3

from queue import Queue
from big_fiubrother_camera.video_chunk_message_publisher import VideoChunkMessagePublisher
from big_fiubrother_camera.camera_factory import build_camera_recoder
from big_fiubrother_core import SignalHandler
from big_fiubrother_core import setup

if __name__ == "__main__":
    configuration = setup('Big Fiubrother Camera Application')
    
    print('[*] Configuring big-fiubrother-camera')

    queue = Queue()
    publisher = VideoChunkMessagePublisher(configuration['publisher'], queue)
    recorder = build_camera_recoder(settings['camera'], queue)
    signal_handler = SignalHandler(callback=recorder.stop)

    print('[*] Configuration finished. Starting big-fiubrother-camera!')
    
    publisher.start()
    recorder.start()

    publisher.stop()
    publisher.wait()
    camera.close()

    print('[*] big-fiubrother-camera stopped!')