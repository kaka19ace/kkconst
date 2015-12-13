#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   ZHONG KAIXIANG <xiang.ace@gmail.com>
# @date     Nov 15 2015
# @brief     
#

"""
USAGE SCENARIO/使用场景:
restful response data:

def get_error_response(request, error_code, extra_message=""):
    # request: web framework request instance
    # error_code: Derived from BaseStatusCode
    # extra_message: python data structure: str, list, dict
    response_data = {
        "status_code": error_code,
        "message": error_code.message,  # for showing to app developer
        "description": error_code.verbose_name,  # maybe for showing to app user

        "extra_message": extra_message,  # more message
    }
    return json_response(request, response_data)

def views(request):
    ...
    return get_error_response(
        request, ServiceStatusCode.SERVICE_UNAVAILABLE, extra_message="help me find the bugs if you can"
    )

"""

import sys
import json
from collections import OrderedDict

from kkconst import (
    BaseConst,
    ConstIntField,
    get_console_logger,
)


PY2 = sys.version_info[0] == 2


class BaseStatusCode(BaseConst):
    class Meta:
        allow_duplicated_value = True  # status_code should be no duplicated value


class StatusCodeField(ConstIntField):
    def __init__(self, status_code, message=u"", description=u""):
        ConstIntField.__init__(status_code, verbose_name=message, description=description)
        self.message = message


class ServiceStatusCode(BaseStatusCode):
    SERVICE_UNAVAILABLE = StatusCodeField(10001, u"service unavailable", description=u"server is sleeping/服务打盹了")


if __name__ == "__main__":
    logger = get_console_logger()

    status_code = ServiceStatusCode.SERVICE_UNAVAILABLE
    assert isinstance(status_code, ConstIntField)
    # assert isinstance(status_code, ConstLongField)  # assert error
    assert isinstance(status_code, int)
    if PY2:
        # assert isinstance(status_code, long)  # assert error, does not support long
        pass

    logger.info(status_code.TYPE)

    logger.info(status_code.verbose_name)
    logger.info(status_code.message)
    logger.info(status_code.description)

    logger.info(type(status_code))
    logger.info(type(status_code.TYPE(status_code)))

    response_data = OrderedDict()
    response_data["status_code"] = status_code
    response_data["message"] = status_code.message
    response_data["description"] = status_code.description
    response_data["extra_message"] = "may you live in an interesting time"
    logger.info(json.dumps(response_data, indent=2))
