# -*- coding:utf-8 -*-

from pykit.enum.boolstrs import BoolStrs


def str2boo(str, strict=True):
    if str.lower() in BoolStrs.TRUE.value:
        return True
    if str.lower() in BoolStrs.FALSE.value:
        return False
    if strict is True:
        raise ValueError('input({}) must be in {}'.format(str, BoolStrs.BOOL.value))
    return False
