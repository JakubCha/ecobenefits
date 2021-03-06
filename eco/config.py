import logging.config
import os

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s %(name)-15s %(levelname)-8s %(processName)-10s %(message)s',
        },
        'sanic': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s - (%(name)s)[%(levelname)s][%(host)s]: %(request)s %(message)s %(status)d %(byte)d',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'api': {
            'class': 'logging.FileHandler',
            'filename': 'api.log',
            'formatter': 'sanic',
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },
        'sanic.root': {
            'handlers': ['console', ],
            'level': 'INFO',
            'propagate': False,
        },
        'sanic': {
            'level': 'INFO',
            'handlers': ['api', ],
            'propagate': False,
        }
    }
}

logging.config.dictConfig(LOG_CONFIG)

HOST = '0.0.0.0'
PORT = 8888

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 5

DB_USER = ''
DB_PASS = ''
DB_NAME = ''
DB_HOST = 'localhost'


FACTORS = [
    'O3',
    'NO2',
    'SO2',
    'PM2.5',
]

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

MODELS_PATH = os.path.join(PROJECT_DIR, 'saved_models/')
DATA_PATH = os.path.join(PROJECT_DIR, 'data/*.csv')
TRAINING_DATA_PATH = os.path.join('data/training_trees.csv')
