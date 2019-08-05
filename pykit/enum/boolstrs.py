# -*- coding:utf-8 -*-

from enum import Enum


class BoolStrs(Enum):
    TRUE = ['true', 't', 'yes', 'y']
    FALSE = ['false', 'f', 'no', 'n']
    BOOL = TRUE + FALSE
