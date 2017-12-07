#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:35:27 2017

@author: mints
"""

from latex_cleanup.checks.basic import BasicCheck


class EnUsUkCheck(BasicCheck):
    NAME = 'US-UK'

    def __init__(self):
        super(EnUsUkCheck, self).__init__()
        self.us_uk = []
        for line in open('en_us_uk.txt', 'r').readlines():
            self.us_uk.append(line.split())

    def simple_check(self, document):
        for us_word, uk_word in self.us_uk:
            if us_word in document.words and uk_word in document.words:
                self.logger.warning(f"both {us_word} and {uk_word} are used")
