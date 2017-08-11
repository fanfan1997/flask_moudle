#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from pythonjsonlogger import jsonlogger


def get_logger(handler='flask'):
    logger = logging.getLogger(handler)
    log_handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter()
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)
    return logger
