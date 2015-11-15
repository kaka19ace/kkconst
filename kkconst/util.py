#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file     util.py
# @author   ZHONG KAIXIANG <xiang.ace@gmail.com>
# @date     Nov 15 2015
# @brief     
#

import sys
import datetime


PY2 = sys.version_info[0] == 2
STRING_TYPES = str if not PY2 else basestring


DATETIME_FORMATS = [
    '%Y-%m-%d %H:%M:%S.%f',
    '%Y-%m-%d %H:%M:%S',
    '%Y-%m-%d',
]


def format_datetime(value):
    datetime_value = None
    for fmt in DATETIME_FORMATS:
        try:
            datetime_value = datetime.datetime.strptime(value, fmt)
        except ValueError:
            pass
        if datetime_value:
            break

    if datetime_value:
        return datetime_value
    else:
        raise ValueError("Could not format datetime value={0} formats={1}".format(value, DATETIME_FORMATS))


def get_real_value(base_type, value):
    real_value = value
    if PY2 and base_type is int and isinstance(value, long) and -sys.maxint <= value <= sys.maxint:
        real_value = int(value)  # force to int

    if base_type is datetime.datetime and isinstance(value, STRING_TYPES):
        real_value = format_datetime(real_value)

    return real_value
