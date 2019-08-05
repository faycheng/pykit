# -*- coding:utf-8 -*-

import os


def mkdirs(path):
    if os.path.exists(path) and os.path.isdir(path):
        return
    if hasattr(os, 'mkdirs'):
        os.makedirs(path)
        return
    os.system('mkdir -p {}'.format(path))


def touch(path):
    if os.path.exists(path) and os.path.isfile(path):
        return
    if not os.path.exists(get_parent_path(path, 1)):
        mkdirs(get_parent_path(path, 1))
    fd = open(path, 'w')
    fd.close()


def get_parent_path(path, depth=1):
    parent_path = path
    for _ in range(depth):
        parent_path = os.path.abspath(os.path.dirname(parent_path))
    return parent_path


def save(content, file):
    mkdirs(get_parent_path(file))
    with open(file, 'w+') as fp:
        fp.write(''.join(content))
