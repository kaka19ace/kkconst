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

import json
from collections import OrderedDict

from kkconst import (
    BaseConst,
    ConstIntField,
    get_console_logger,
)


class StatusCodeField(ConstIntField):
    def __init__(self, status_code, message=u"", description=u""):
        ConstIntField.__init__(status_code, verbose_name=message, description=description)
        self.message = message


class BaseStatusCode(BaseConst):
    @classmethod
    def get_message(cls, status_code, default=None):
        return cls.get_verbose_name(status_code, default=default)


class ServiceStatusCode(BaseStatusCode):
    SERVICE_UNAVAILABLE = StatusCodeField(10001, u"service unavailable", description=u"server is sleeping/服务打盹了")


if __name__ == "__main__":
    logger = get_console_logger()

    error_code = ServiceStatusCode.SERVICE_UNAVAILABLE
    assert isinstance(error_code, ConstIntField)
    assert isinstance(error_code, int)

    logger.info(error_code.TYPE)

    logger.info(error_code.verbose_name)
    logger.info(error_code.message)
    logger.info(error_code.description)

    logger.info(ServiceStatusCode.get_message(error_code))
    logger.info(ServiceStatusCode.get_message(error_code))

    logger.info(type(error_code))
    logger.info(type(error_code.TYPE(error_code)))

    logger.info(ServiceStatusCode.get_verbose_name(error_code))
    logger.info(ServiceStatusCode.get_verbose_name(error_code.TYPE(error_code)))

    response_data = OrderedDict()
    response_data["status_code"] = error_code
    response_data["message"] = error_code.message
    response_data["description"] = error_code.description
    response_data["extra_message"] = "may you live in an interesting time"
    logger.info(json.dumps(response_data, indent=2))
