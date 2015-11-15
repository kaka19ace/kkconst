***********************
kkconst: const util lib
***********************

**kkconst** is a constant-tools library.

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

Get It Now
==========

::

    $ pip install kkconst

Project Links
=============

- GitHub: https://github.com/kaka19ace/kkconst
- PyPi: https://pypi.python.org/pypi/kkconst

License
=======

MIT licensed. See the bundled `LICENSE <https://github.com/kaka19ace/kkconst/blob/master/LICENSE>`_ file for more details.

Requirements
============

- Python >= 2.7 or >= 3.4
