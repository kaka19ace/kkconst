#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   ZHONG KAIXIANG  <xiang.ace@gmail.com>
# @date     Nov 15 2015
# @brief     
#

import sys
from kkconst import (
    BaseConst,
    ConstStringField,
    ConstUnicodeField,
    get_console_logger,
)

PY2 = sys.version_info[0] == 2

# PY3: ConstUnicodeField is ConstStringField


class SystemMessage(BaseConst):
    SERVICE_UNAVAILABLE = ConstUnicodeField(u"service unavailable", verbose_name=u"Service is sleeping/服务睡眠中")
    # SERVICE_UNAVAILABLE = ConstStringField(u"service unavailable", verbose_name=u"Service is sleeping/服务睡眠中")
    PERMISSION_DENY = ConstUnicodeField(u"permission deny", verbose_name=u"your have no permission/你的权限被拒绝")
    # PERMISSION_DENY = ConstStringField(u"permission deny", verbose_name=u"your have no permission/你的权限被拒绝")


if __name__ == "__main__":
    """ just test unicode """

    logger = get_console_logger()
    message = SystemMessage.SERVICE_UNAVAILABLE

    if PY2:
        assert isinstance(message, ConstUnicodeField)
        assert isinstance(message, unicode)
    else:
        assert isinstance(message, ConstUnicodeField)
        assert isinstance(message, ConstStringField)
        assert isinstance(message, str)

    logger.info(message)
    logger.info(message.TYPE)
    logger.info(type(message))
    logger.info(type(message.TYPE(message)))

    logger.info(message.verbose_name)
    logger.info(SystemMessage.get_verbose_name(message))
    logger.info(SystemMessage.get_verbose_name(message.TYPE(message)))
    logger.info(SystemMessage.get_verbose_name(u"service unavailable"))
    logger.info(SystemMessage.get_verbose_name(u"服务异常"))  # should be None
    # if PY2 and const value has non english language, you should check unicode and str
    # eg: logger.info(SystemMessage.get_verbose_name(u"服务异常"))
