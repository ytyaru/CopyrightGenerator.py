#!/usr/bin/env python3
# coding: utf8
import datetime
class Copyright:
    DEFAULT_NAME = '{{AuthorName}}'
    @classmethod
    def Generate(cls, name=None):
        if name is None: name = cls.DEFAULT_NAME
        if not isinstance(name, str): raise TypeError('name should be of type str.')
        return '© {} {}'.format(datetime.datetime.now().strftime('%Y'), name)

    def __init__(self, default_name='{{AuthorName}}'):
        self.DefaultName = Copyright.DEFAULT_NAME if default_name is None else  default_name
    @property
    def DefaultName(self): return self.__default_name
    @DefaultName.setter
    def DefaultName(self, value):
        if not isinstance(value, str): raise TypeError('DefaultName should be of type str.')
        self.__default_name = value
    def generate(self, name=None):
        if name is None: name = self.__default_name
        if not isinstance(name, str): raise TypeError('name should be of type str.')
        return '© {} {}'.format(datetime.datetime.now().strftime('%Y'), name)


if __name__ == '__main__':
    def get_default_name():
        import sys,os
        if 1 < len(sys.argv): return sys.argv[1]
        elif 'AUTHOR_NAME' in os.environ.keys(): return os.environ['AUTHOR_NAME']
        elif 'AUTHOR' in os.environ.keys(): return os.environ['AUTHOR']
        else : return None
    print(Copyright.Generate(get_default_name()))       
