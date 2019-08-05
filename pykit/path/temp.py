# -*- coding:utf-8 -*-

import os
import uuid
from shutil import copyfile


class TempDir(object):
    pass


class TempFile(object):
    def __init__(self, name=None, suffix='tmp'):
        self.path = '/tmp/{}.{}'.format(name or str(uuid.uuid4()), suffix)
        self._fd = None
        self._close = False

    @property
    def fd(self):
        return self._fd

    def close(self):
        if self._close is True:
            return
        self.fd.close()
        self._close = True

    def __enter__(self):
        self._fd = open(self.path, 'w+')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        os.remove(self.path)


class TempPipe(TempFile):
    def __init__(self, name=None):
        super(TempPipe, self).__init__(name, suffix='pipe')

    @property
    def pipe(self):
        if self._fd is None:
            self._fd = open(self.path, 'wb+')
        return self._fd


class TempFileCopy(TempFile):
    def __init__(self, path, suffix='tmp', mode='r'):
        self.origin = path
        self.path = '{}.{}'.format(path, suffix)
        self.mode = mode
        self._fd = None
        self._close = False

    def _copy(self):
        copyfile(self.origin, self.path)

    def __enter__(self):
        self._copy()
        self._fd = open(self.path, self.mode)
        return self


if __name__ == '__main__':
    with TempFileCopy(__file__) as f:
        print(f.fd.read())
