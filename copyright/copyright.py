#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform
vers = platform.python_version_tuple()
if   2 >= int(vers[0]): from py2.copyright import *
elif 3 <= int(vers[0]): from py3.copyright import *
else: raise Exception('There is no source code corresponding to the specified Python version.')
