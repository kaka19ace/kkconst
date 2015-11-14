#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @author   ZHONG KAIXIANG <xiang.ace@gmail.com>
# @date     Nov 14 2015
# @brief
#


from six import (
    with_metaclass,
    PY2,
)


class _RawConstField(object):
    _SUPPORT_TYPES = (int, float, str, bytes)
    if PY2:
        _SUPPORT_TYPES += (unicode,)  # awesome

    _REGISTERED_FIELD_DICT = {}  # type: const_cls

    def __call__(self, base_type):
        const_field = self._REGISTERED_FIELD_DICT.get(base_type)
        if const_field:
            return const_field

        class ConstField(base_type):
            TYPE = base_type

            def __new__(const_cls, value, verbose_name=u"", **kwargs):
                if type(value) not in self._SUPPORT_TYPES:
                    raise TypeError("const field only support types={0}".format(self._SUPPORT_TYPES))

                if not isinstance(value, base_type):
                    raise TypeError(
                        "const field value={0} v_type={1} not match type={2}".format(value, type(value), const_cls.TYPE)
                    )

                obj = base_type.__new__(const_cls, value)
                kwargs["verbose_name"] = verbose_name
                obj.__dict__.update(**kwargs)
                return obj

        self._REGISTERED_FIELD_DICT[base_type] = ConstField
        return ConstField

    @property
    def registered_field_types(self):
        return list(self._REGISTERED_FIELD_DICT.values())


_ConstField = _RawConstField()


class _Mixin(object):
    # just for ide code intellisense :)
    TYPE = NotImplemented
    verbose_name = NotImplemented


class ConstIntField(_ConstField(int), _Mixin):
    pass

if PY2:
    class ConstLongField(_ConstField(long), _Mixin):
        pass
else:
    ConstLongField = ConstIntField


class ConstFloatField(_ConstField(float), _Mixin):
    pass


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
