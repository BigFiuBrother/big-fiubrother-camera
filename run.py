#!/usr/bin/env python3

import yaml
import argparse
from queue import Queue
from big_fiubrother_camera.video_chunk_message_publisher import VideoChunkMessagePublisher
from big_fiubrother_camera.camera_factory import build_camera_recoder
from big_fiubrother_core import SignalHandler


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Big Fiubrother Camera Application')
    parser.add_argument('environment', type=str, nargs='?', default='development', help='Environment to run applicacion. By default it is development.')

    args = parser.parse_args()

    print('[*] Configuring big-fiubrother-camera')

    with open('config/{}.yml'.format(args.environment.lower())) as config_file:    
        configuration = yaml.safe_load(config_file)

    queue = Queue()
    message_client = VideoChunkMessageProducer(configuration['message_client'], queue)
    camera_recorder = build_camera_recoder(settings['camera'], queue)
    signal_handler = SignalHandler(callback=camera_recorder.stop)

    print('[*] Configuration finished. Starting big-fiubrother-camera!')
    
    message_client.start()
    camera_recorder.start()

    message_client.stop()
    message_client.wait()
    camera.close()

    print('[*] big-fiubrother-camera stopped!')