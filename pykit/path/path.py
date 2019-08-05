# -*- coding:utf-8 -*-

import os

from pykit.path.helper import get_parent_path


class Path(object):
    def __init__(self, path):
        self.abs_path = os.path.abspath(path)
        if not os.path.exists(path):
            raise IOError('No such file or directory: {}'.format(self.abs_path))

    @property
    def parent_dir(self):
        return get_parent_path(self.abs_path, 1)

    @property
    def is_dir(self):
        return os.path.isdir(self.abs_path)

    @property
    def is_file(self):
        return os.path.isfile(self.abs_path)

    @property
    def name(self):
        return self.abs_path.split('/')[-1]

    @property
    def extension_name(self):
        if self.is_dir:
            raise TypeError('Path type must be file')
        if '.' not in self.name:
            return ''
        return self.name.split('.')[-1]


