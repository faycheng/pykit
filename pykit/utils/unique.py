# -*- coding:utf-8 -*-

import types
from functools import wraps


def _compare(item, another, key_func=None):
    if key_func is None:
        return item == another
    try:
        return key_func(item) == key_func(another)
    except AttributeError:
        return False


def _iter(obj, key_func=None):
    obj = sorted(obj, key=key_func)
    last = object()
    for item in obj:
        if _compare(item, last, key_func) is True:
            continue
        yield item
        last = item


def unique(key_func=None):
    def func_decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            if not (isinstance(res, list) or isinstance(res, types.GeneratorType)):
                return res
            return _iter(res, key_func)

        return inner

    return func_decorator
