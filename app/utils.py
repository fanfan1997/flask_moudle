#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import logging.config
from pythonjsonlogger import jsonlogger
from config import config


def get_logger(handler='flask'):
    logger = logging.getLogger(handler)
    logging.config.dictConfig(config[os.getenv('config') or 'default'].LOGGING)
    log_handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger
