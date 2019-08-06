# -*- coding:utf-8 -*-

from prompt_toolkit.history import FileHistory


class PromptFileHistory(FileHistory):
    def append(self, string):
        if not string or len(string) > 80:
            return
        super(PromptFileHistory, self).append(string)
