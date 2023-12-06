import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    client_id = os.environ.get('client_id')
    client_sec = os.environ.get('client_sec')
