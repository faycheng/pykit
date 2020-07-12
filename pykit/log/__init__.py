# -*- coding:utf-8 -*-
import logging
import os

LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARN': logging.WARN,
    'ERROR': logging.ERROR
}
LOG_LEVEL = LOG_LEVELS.get(os.getenv('LOG_LEVEL', None).upper(), logging.DEBUG)

STD_LOG = logging.getLogger('STD_LOG')
STD_LOG.propagate = False
STD_LOG.setLevel(LOG_LEVEL)
STD_LOG_FORMATTER = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
STD_HANDLER = logging.StreamHandler()
STD_HANDLER.setFormatter(STD_LOG_FORMATTER)
STD_LOG.addHandler(STD_HANDLER)
