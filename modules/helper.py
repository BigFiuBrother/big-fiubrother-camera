import logging
import os

LOGGING_LEVELS = {
    'DEBUG': 10,
    'INFO': 20,
    'WARNING': 30,
    'ERROR': 40,
}

def configure_logger(settings):
    if not os.path.exists('./log/'):
        os.makedirs('./log/')

    logging.basicConfig(level=LOGGING_LEVELS[settings['level']],
                        format='%(asctime)s %(levelname)-8s {} %(message)s'.format(os.getpid()),
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='./log/camera.log',
                        filemode='a')

    logging.getLogger('pika').setLevel(logging.WARNING)
