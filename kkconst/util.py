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

try:
    from six import with_metaclass
except:
    def with_metaclass(meta, *bases):
        """Create a base class with a metaclass. copy from six """
        class metaclass(meta):
            def __new__(cls, name, this_bases, d):
                return meta(name, bases, d)
        return type.__new__(metaclass, 'temporary_class', (), {})

try:
    from cached_property import cached_property
except:
    class cached_property(object):
        """ https://github.com/bottlepy/bottle/blob/master/bottle.py """
        def __init__(self, func):
            self.__doc__ = getattr(func, '__doc__')
            self.func = func

        def __get__(self, obj, cls):
            if obj is None:
                return self
            value = obj.__dict__[self.func.__name__] = self.func(obj)
            return value


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
