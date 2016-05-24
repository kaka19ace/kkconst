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


New Features
============
**1.1.3**
    1. bugfix
**1.1.2**
    1. fixed demos code
**1.1.0**
    1. Meta support 'strict_capital' attribute to require const class's const variable capital naming.


Example
=======

**int: status_code**

.. code-block:: python

    from __future__ import print_function
    import json
    from collections import OrderedDict
    from kkconst import BaseConst, ConstIntField

    class BaseStatusCode(BaseConst):
        class Meta:
            allow_duplicated_value = False  # status_code should be no duplicated value


    class StatusCodeField(ConstIntField):
        def __init__(self, status_code, message=u"", description=u""):
            ConstIntField.__init__(status_code, verbose_name=message, description=description)
            self.message = message


    class ServiceStatusCode(BaseStatusCode):
        SERVICE_UNAVAILABLE = StatusCodeField(10001, u"service unavailable", description=u"server is sleeping/服务打盹了")


    status_code = ServiceStatusCode.SERVICE_UNAVAILABLE
    assert isinstance(status_code, ConstIntField)
    assert isinstance(status_code, int)

    print(status_code.verbose_name) # "service unavailable"
    print(status_code.description)  # "server is sleeping"

    # for restful response
    response_data = OrderedDict()
    response_data["status_code"] = status_code
    response_data["message"] = status_code.verbose_name  # also status_code.message is the same value
    response_data["description"] = status_code.description
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


**BaseConst: Your Const Helper**
    like peewee model' Meta, we can use Meta to help manage the const variable

.. code-block:: python

    the Meta support such attributes:

    allow_duplicated_value - bool
        default True,
        when set False, if exists a variable has the same as the another variable defined before,
        then raise AttributeError

    strict_capital - bool
        default True, the ConstClass will check the const variable name,
        if name is not upper, then raise AttributeError

.. code-block:: python

    class ErrorCode(BaseConst):
        class Meta:
            allow_duplicated_value = False
            strict_capital = True

        USER_ID_NOT_EXISTS = ConstIntField(20001, verbose_name="USER_ID_ERROR")

        # will raise Error, because has the same with USER_ID_NOT_EXISTS
        # USER_EMAIL_INVALID = ConstIntField(20001, verbose_name="USER_EMAIL_ERROR")

        # will raise Error, because some letters are lowercase
        # User_Password_Invalid = ConstIntField(20003, verbose_name="USER_PASSWORD_ERROR")


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
