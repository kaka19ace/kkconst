***********************
kkconst: const util lib
***********************

**kkconst** is a constant-tools library.

Project Links
=============

- GitHub: https://github.com/kaka19ace/kkconst
- PyPi: https://pypi.python.org/pypi/kkconst

Support Types:
==============
int, str, bytes, datetime

In PY2: with unicode

Example
=======

**int: status_code**

.. code-block:: python

    from __future__ import print_function
    import json
    from collections import OrderedDict
    from kkconst import BaseConst, ConstIntField

    class BaseStatusCode(BaseConst):
        pass

    class ServiceStatusCode(BaseStatusCode):
        SERVICE_UNAVAILABLE = ConstIntField(10001, u"service unavailable", description=u"server is sleeping")

    error_code = ServiceStatusCode.SERVICE_UNAVAILABLE
    assert isinstance(error_code, ConstIntField)
    assert isinstance(error_code, int)

    print(error_code.verbose_name) # "service unavailable"
    print(error_code.description)  # "server is sleeping"
    print(ServiceStatusCode.get_verbose_name(error_code))  # "service unavailable"

    # for restful response
    response_data = OrderedDict()
    response_data["status_code"] = error_code
    response_data["message"] = error_code.message
    response_data["description"] = error_code.description
    response_data["extra_message"] = "may you live in an interesting time"
    print(json.dumps(response_data, indent=2))
    # {
    #    "status_code": 10001,
    #    "message": "service unavailable",
    #    "description": "server is sleeping",
    #    "extra_message": "may you live in an interesting time"
    # }
    #
    # def views(request):
    #     ...
    #     return HttpResponse(200, response_data, "application/json")
    #

**float: math constant**

.. code-block:: python

    from __future__ import print_function
    from kkconst import (
        BaseConst,
        ConstFloatField,
        get_console_logger,
    )

    class MathConst(BaseConst):
        PI = ConstFloatField(3.1415926, verbose_name=u"Pi")
        E = ConstFloatField(2.7182818284, verbose_name=u"mathematical constant")  # Euler's number"
        GOLDEN_RATIO = ConstFloatField(0.6180339887, verbose_name=u"Golden Ratio")

    magic_num = MathConst.GOLDEN_RATIO
    assert isinstance(magic_num, ConstFloatField)
    assert isinstance(magic_num, float)

    print(magic_num)  # 0.6180339887
    print(magic_num.verbose_name)  # Golden Ratio
    print(MathConst.get_verbose_name(magic_num))  # Golden Ratio
    print(MathConst.get_verbose_name(magic_num.TYPE(magic_num)))  # Golden Ratio
    print(MathConst.get_verbose_name(0.6180339887))  # Golden Ratio
    print(MathConst.get_verbose_name(0.618033988))  # None
    print(MathConst.get_verbose_name(0.618))  # None

**str: system message**

.. code-block:: python

    from kkconst import BaseConst, ConstStringField
    # Python3 ConstStringField is equal to ConstUnicodeField
    class SystemMessage(BaseConst):
        SERVICE_UNAVAILABLE = ConstStringField(u"service unavailable", verbose_name=u"Service is sleeping")
        PERMISSION_DENY = ConstStringField(u"permission deny", verbose_name=u"your have no permission")

**datetime: released datetime**

.. code-block:: python

    class ReleasedDatetime(BaseConst):
        PYTHON_2_0 = ConstDatetimeField("2000-10-16", verbose_name="PY2 Released")
        PYTHON_3_0 = ConstDatetimeField(datetime.datetime(year=2008, month=12, day=3), verbose_name="PY3 Released")

    released_datetime = ReleasedDatetime.PYTHON_2_0
    assert isinstance(field_value, ConstDatetimeField)
    assert isinstance(field_value, datetime.datetime)

    print(field_value)
    print(field_value.verbose_name)  # "PY2 Released"
    print(ReleasedDatetime.get_verbose_name(field_value))  # "PY2 Released"

    print(ReleasedDatetime.get_verbose_name(field_value.TYPE(**field_value.to_dict())))
    # param type is datetime
    # output: PY2 Released

    print(ReleasedDatetime.get_verbose_name(datetime.datetime(year=2000, month=10, day=16)))
    # if raw_field_value is str, output None
    # output: PY2 Released


Get It Now
==========

::

    $ pip install kkconst


License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/kaka19ace/kkconst/blob/master/LICENSE>`_ file for more details.

Requirements
============

- Python >= 2.7 or >= 3.4
