#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check for spelling out numbers below 11.
Created on 23.11.2023

@author: mints
"""
import re
from latex_cleanup.checks.basic import BasicCheck
from astropy import units as u


class NumbersCheck(BasicCheck):
    NAME = 'Numbers'
    REGISTRY = set()

    def __init__(self):
        super(NumbersCheck, self).__init__()
        self.REGISTRY |= set(u.get_current_unit_registry()._registry.keys())
        self.table_mode = False

    def simple_check(self, document):
        after_number = False
        number_word = ''

        for line_number, line in enumerate(document.text):
            if line.strip().startswith('\\begin{tab'):
                self.table_mode = True
                continue
            elif line.strip().startswith('\\end{tab'):
                self.table_mode = False
                continue
            elif self.table_mode:
                continue
            for word in document.splitter.split(line.strip().lower()):
                if (word.isnumeric() and len(word) == 1) or word == '10':
                    after_number = True
                    number_word = word
                    continue
                elif after_number and word not in self.REGISTRY:
                    self.logger.warning(f"'{number_word}' in line {line_number} should be spelled out, if not followed by a unit.")
                after_number = False

