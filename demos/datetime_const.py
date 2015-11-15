#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file     datetime_const.py
# @author   ZHONG KAIXIANG <xiang.ace@gmail.com>
# @date     Nov 15 2015
# @brief     
#

import datetime

from kkconst import (
    BaseConst,
    ConstDatetimeField,
    get_console_logger,
)


class ReleasedDatetime(BaseConst):
    PYTHON_2_0 = ConstDatetimeField("2000-10-16", verbose_name="PY2 Released")
    PYTHON_3_0 = ConstDatetimeField(datetime.datetime(year=2008, month=12, day=3), verbose_name="PY3 Released")


if __name__ == "__main__":
    logger = get_console_logger()

    def check(field_value, raw_field_value):
        assert isinstance(field_value, ConstDatetimeField)
        assert isinstance(field_value, datetime.datetime)

        logger.info(field_value)
        logger.info(field_value.TYPE)
        logger.info(type(field_value))
        logger.info(type(field_value.TYPE(**field_value.to_dict())))

        logger.info(field_value.verbose_name)
        logger.info(ReleasedDatetime.get_verbose_name(field_value))
        logger.info(ReleasedDatetime.get_verbose_name(field_value.TYPE(**field_value.to_dict())))

        logger.info(ReleasedDatetime.get_verbose_name(raw_field_value))  # if raw_field_value is str, output None

    released_datetime = ReleasedDatetime.PYTHON_2_0
    check(released_datetime, "2000-10-16")  # raw_field_value could not get verbose_name, only support datetime.datetime

    released_datetime = ReleasedDatetime.PYTHON_3_0
    check(released_datetime, datetime.datetime(year=2008, month=12, day=3))
