#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @file     const_float.py
# @author   kaka_ace <xiang.ace@gmail.com>
# @date     Nov 15 2015
# @brief     
#

from kkconst import (
    BaseConst,
    ConstFloatField,
    get_console_logger,
)


class MathConst(BaseConst):
    PI = ConstFloatField(3.1415926, verbose_name=u"Pi")
    E = ConstFloatField(2.7182818284, verbose_name=u"mathematical constant")  # Euler's number"
    GOLDEN_RATIO = ConstFloatField(0.6180339887, verbose_name=u"Golden Ratio")


if __name__ == "__main__":
    """ just test unicode """

    logger = get_console_logger()
    magic_num = MathConst.GOLDEN_RATIO

    assert isinstance(magic_num, ConstFloatField)
    assert isinstance(magic_num, float)

    logger.info(magic_num)
    logger.info(magic_num.TYPE)
    logger.info(type(magic_num))
    logger.info(type(magic_num.TYPE(magic_num)))

    logger.info(magic_num.verbose_name)
    logger.info(MathConst.get_verbose_name(magic_num))
    logger.info(MathConst.get_verbose_name(magic_num.TYPE(magic_num)))
    logger.info(MathConst.get_verbose_name(0.6180339887))  # Golden Ratio
    logger.info(MathConst.get_verbose_name(0.618033988))  # None
    logger.info(MathConst.get_verbose_name(0.618))  # None

