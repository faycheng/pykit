# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import random
import uuid
import types
import string


def random_lower_string(length=8):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def random_upper_string(length=8):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(length))


def random_number_string(length=8):
    return ''.join(random.choice(string.digits) for _ in range(length))


def random_string(length=8):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def random_uuid():
    return str(uuid.uuid4())


# Invoker: xxxx
# Arguments: xxxx
# Return: xxxx
# Exception: xxx
def random_enum(enum_list=None):
    if isinstance(enum_list, types.GeneratorType):
        return random.choice(list(enum_list))
    return random.choice(enum_list)




def random_number(min, max):
    return random.randint(min, max)
