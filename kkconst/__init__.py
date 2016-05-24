#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   ZHONG KAIXIANG <xiang.ace@gmail.com>
# @date     Nov 15 2015
# @brief
#

import sys
import logging

from .const import (
    BaseConst,
    ConstIntField,
    ConstFloatField,
    ConstStringField,
    ConstBytesField,
    ConstUnicodeField,
    ConstDatetimeField,
)

__version__ = "1.1.3"

__console_logger = None


def get_console_logger():
    """ just for kkconst demos """
    global __console_logger
    if __console_logger:
        return __console_logger

    logger = logging.getLogger("kkconst")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    __console_logger = logger

    return logger

