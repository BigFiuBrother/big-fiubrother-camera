import os

TMP = 'tmp'
FORMAT = 'h264'


def create_local_storage():
    if os.path.exists(TMP):
        os.mkdir(TMP)


def get_filename(timestamp):
    return os.path.join(TMP, f'{timestamp}.{FORMAT}')


def delete_video(timestamp):
    os.remove(get_filename(timestamp))
