# -*- coding:utf-8 -*-

from enum import Enum
from prompt_toolkit.completion import Completion, Completer
from candy_utils.unique import unique
from candy_path import iter as p_iter


class WordMatchType(object):
    CONTAINS = 'CONTAINS'
    STARTSWITH = 'STARTSWITH'


class WordCompleter(Completer):
    def __init__(self, words=None, history=None, match_type=WordMatchType.CONTAINS):
        self.words = words or []
        self.history = history or []
        self.match_type = match_type
        self.lower = False

    def match(self, text_before_cursor, word):
        if self.match_type == WordMatchType.CONTAINS:
            return text_before_cursor in word

    # utils unique 只能保证 custom & history 各自的列表中不出现重复，无法保证 custom & history 没有交集
    @unique(lambda completion: completion.text)
    def get_completions(self, document, complete_event):
        if self.lower is False:
            self.words = [word.lower() for word in self.words]
            self.history = [record.lower() for record in self.history]
            self.lower = True
        text_before_cursor = document.text_before_cursor.lower()
        for word in self.words:
            if self.match(text_before_cursor, word):
                display_meta = '    custom'
                yield Completion(word, -len(text_before_cursor), display_meta=display_meta)
        for record in self.history:
            if self.match(text_before_cursor, record):
                display_meta = '    history'
                yield Completion(record, -len(text_before_cursor), display_meta=display_meta)


class PathMatchType(Enum):
    DIRS = p_iter.list_dirs
    FILES = p_iter.list_files
    ALL = p_iter.list_all


class PathCompleter(Completer):
    def __init__(self, root, match_type='ALL', recursion=False):
        self.root = root
        self.match_type = match_type.upper()
        self.recursion = recursion

    @unique(lambda completion: completion.text)
    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor.lower()
        list_paths = getattr(PathMatchType, self.match_type).value
        for p in list_paths(self.root, recursion=self.recursion):
            if text_before_cursor in p.lower():
                yield Completion(p, start_position=-len(text_before_cursor), display_meta=self.match_type)
            p_name = p.rstrip('/').split('/')[-1]
            if text_before_cursor in p_name.lower():
                yield Completion(p, start_position=-len(text_before_cursor), display_meta=self.match_type)
