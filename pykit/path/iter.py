# -*- coding:utf-8 -*-

import os


def list_dirs(path, recursion=True):
    assert os.path.exists(path) and os.path.isdir(path)
    if recursion is True:
        for dir_path, dir_names, _ in os.walk(path):
            for dir_name in dir_names:
                yield os.path.join(dir_path, dir_name)
    if recursion is False:
        for dir in [p for p in os.listdir(path) if os.path.isdir(os.path.join(path, p))]:
            yield os.path.join(path, dir)


def list_files(path, recursion=True):
    assert os.path.exists(path) and os.path.isdir(path)
    if recursion is True:
        for dir_path, _, file_names in os.walk(path):
            for file_name in file_names:
                yield os.path.join(dir_path, file_name)
    if recursion is False:
        for file in [p for p in os.listdir(path) if os.path.isfile(os.path.join(path, p))]:
            yield os.path.join(path, file)


def list_all(path, recursion=True):
    assert os.path.exists(path) and os.path.isdir(path)
    if recursion is True:
        for dir in list_dirs(path):
            yield dir
        for file in list_files(path):
            yield file
    if recursion is False:
        for p in os.listdir(path):
            yield os.path.join(path, p)
