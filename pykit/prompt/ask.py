# -*- coding:utf-8 -*-

from pykit.prompt import prompt


def ask(msg, expect, default, error):
    value = prompt.prompt_list("{}\nYes/No:\n".format(msg), type="STR", default=default, use_history=False,
                               completions=['yes', 'no'])
    if value == expect:
        return True
    if error is None:
        return value == expect
    raise error


def ask_yes(msg, error=None):
    return ask(msg, "yes", "no", error)
