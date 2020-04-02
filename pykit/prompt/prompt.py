# -*- coding:utf-8 -*-

import os
import sys
import ast

# sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import prompt_toolkit
import pykit.path as path

from pykit.prompt.completer import *
from pykit.prompt.validator import *
from pykit.prompt.history import PromptFileHistory as FileHistory
from enum import Enum

class PromptType(Enum):
    STR = StrValidator()
    INT = IntValidator()
    BOOL = BoolValidator()
    FLOAT = FloatValidator()
    LIST = ListValidator()
    DICT = ListValidator()
    DIR = DirValidator()
    FILE = FileValidator()


def _convert(data, type):
    return ast.literal_eval(data) if type.upper() in ['INT', 'BOOL', 'FLOAT', 'LIST', 'DICT'] else data


def prompt(message, type='STR', default=None, multiline=False, history=None):
    history = FileHistory(history or os.path.join(path.HOME, '.prompt_history'))
    converter = getattr(PromptType, type)
    completer = WordCompleter(words=[], history=history)
    res = prompt_toolkit.prompt(message, default=default or '', history=history,
                                validator=converter.value, completer=completer, multiline=multiline)
    return _convert(res, type)


def prompt_list(message, type='STR', default=None, completions=None, multiline=False, use_history=True, history=None):
    history = FileHistory(history or os.path.join(path.HOME, '.prompt_history'))
    if use_history is False:
        history = []
    converter = getattr(PromptType, type)
    completer = WordCompleter(words=completions, history=history)
    res = prompt_toolkit.prompt(message, default=default or '', history=history,
                                validator=converter.value, completer=completer, multiline=multiline)
    return _convert(res, type)


def prompt_path(message, root, type='DIR', recursion=False, default=None):
    converter = getattr(PromptType, type)
    completer = PathCompleter(root, match_type=type, recursion=recursion)
    res = prompt_toolkit.prompt(message, default=default or '', completer=completer,
                                validator=converter.value)
    return _convert(res, 'STR')

