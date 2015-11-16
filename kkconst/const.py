#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   ZHONG KAIXIANG <xiang.ace@gmail.com>
# @date     Nov 14 2015
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


PY2 = sys.version_info[0] == 2
STRING_TYPES = str if not PY2 else basestring
_DATETIME_FORMATS = [
        '%Y-%m-%d %H:%M:%S.%f',
        '%Y-%m-%d %H:%M:%S',
        '%Y-%m-%d',
]


def _format_datetime(value):
    datetime_value = None
    for fmt in _DATETIME_FORMATS:
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


def _get_real_value(base_type, value):
    real_value = value
    if PY2 and base_type is int and isinstance(value, long) and -sys.maxint <= value <= sys.maxint:
        real_value = int(value)  # force to int

    if base_type is datetime.datetime and isinstance(value, STRING_TYPES):
        real_value = _format_datetime(real_value)

    return real_value


class _RawConstField(object):
    SUPPORT_TYPES = (int, float, str, bytes, datetime.datetime,)
    if PY2:
        SUPPORT_TYPES += (unicode,)  # awesome

    _REGISTERED_FIELD_DICT = {}  # type: const_cls

    def __call__(self, base_type):
        const_field = self._REGISTERED_FIELD_DICT.get(base_type)
        if const_field:
            return const_field

        const_field_cls = self._create_const_field_cls(base_type)
        self._REGISTERED_FIELD_DICT[base_type] = const_field_cls
        return const_field_cls

    @classmethod
    def _create_const_field_cls(cls, base_type):
        class ConstField(base_type):
            TYPE = base_type

            def __new__(const_cls, value=None, verbose_name=u"", **kwargs):
                real_value = _get_real_value(base_type, value)

                if type(real_value) not in cls.SUPPORT_TYPES:
                    raise TypeError(
                        "const field only support types={0} value={1} real_value={2}".format(
                            cls._SUPPORT_TYPES, value, real_value
                        )
                    )

                if not isinstance(real_value, base_type):
                    raise TypeError(
                        "const field real_value={0} v_type={1} value={2} not match type={3}".format(
                            real_value, value, type(value), const_cls.TYPE
                        )
                    )

                obj = _RawConstField._new_obj(base_type, real_value, const_cls, **kwargs)
                obj.verbose_name = verbose_name
                return obj
        return ConstField

    @staticmethod
    def _new_obj(base_type, value, const_cls, **kwargs):
        if base_type is datetime.datetime:
            kwargs["year"], kwargs["month"], kwargs["day"] = value.year, value.month, value.day
            kwargs["hour"], kwargs["minute"], kwargs["second"] = value.hour, value.minute, value.second
            kwargs["microsecond"] = value.microsecond
            kwargs["tzinfo"] = value.tzinfo
            obj = datetime.datetime.__new__(const_cls, **kwargs)
        else:
            obj = base_type.__new__(const_cls, value)
            obj.__dict__.update(**kwargs)
        return obj

    @property
    def registered_field_types(self):
        return list(self._REGISTERED_FIELD_DICT.values())


_ConstField = _RawConstField()


class _Mixin(object):
    # just for ide code intellisense :)
    TYPE = NotImplemented
    verbose_name = NotImplemented


# number
class ConstIntField(_ConstField(int), _Mixin):
    """ no support long type, the const value <= sys.maxint at PY2"""


class ConstFloatField(_ConstField(float), _Mixin):
    pass


# str/unicode
class ConstStringField(_ConstField(str), _Mixin):
    pass

if PY2:
    ConstBytesField = ConstStringField

    class ConstUnicodeField(_ConstField(unicode), _Mixin):
        pass
else:
    class ConstBytesField(_ConstField(bytes), _Mixin):
        pass

    ConstUnicodeField = ConstStringField


# datetime
class ConstDatetimeField(_ConstField(datetime.datetime), _Mixin):
    FORMATS = _DATETIME_FORMATS

    def to_dict(self):
        return dict(
            year=self.year, month=self.month, day=self.day,
            hour=self.hour, minute=self.minute, second=self.second,
            microsecond=self.microsecond, tzinfo=self.tzinfo
        )


class ConstMetaClass(type):
    def __new__(cls, name, bases, namespace):
        verbose_name_dict = {}
        const_field_types = tuple(_ConstField.registered_field_types)
        for k, v in namespace.items():
            # just check base const field by _ConstFieldHelper.get_const_filed_class(xxx)
            if getattr(v, '__class__', None) and isinstance(v, const_field_types):
                verbose_name_dict[v] = getattr(v, 'verbose_name', "")
        namespace["_verbose_name_dict"] = verbose_name_dict
        return type.__new__(cls, name, bases, namespace)

    def __setattr__(self, key, value):
        raise AttributeError("Could not set ConstField {key} {value} again".format(key=key, value=value))


class BaseConst(with_metaclass(ConstMetaClass)):
    """ Abstract Class """
    _verbose_name_dict = NotImplemented

    @classmethod
    def get_verbose_name(cls, const_value, default=None):
        return cls._verbose_name_dict.get(const_value, default)