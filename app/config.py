import os


class LocalConfig(object):
    ENV = 'local'
    DATABASE_URI = 'file:app.db'
    DEBUG = True


class TestConfig(object):
    ENV = 'test'
    DATABASE_URI = 'file::memory:?cache=shared'
    DEBUG = True

CONFIGS = {
    'local': LocalConfig,
    'test': TestConfig,
}


def get_config(env):
    return CONFIGS.get(env)


def get_current_config():
    return get_config(os.environ['APP_ENV'])
