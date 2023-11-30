#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:35:27 2017

@author: mints
"""
import re
from latex_cleanup.checks.basic import BasicCheck


class TodoCheck(BasicCheck):
    NAME = 'Todo'

    def __init__(self):
        super(TodoCheck, self).__init__()

    def simple_check(self, document):
        for todo in re.findall(r'todo:([^.]*)\.', ' '.join(document.text), flags=re.IGNORECASE):
             self.logger.error("TODO: %s" % todo)

