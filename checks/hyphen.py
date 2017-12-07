#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:01:57 2017

@author: mints
"""

from latex_cleanup.checks.basic import BasicCheck


class HyphenCheck(BasicCheck):
    NAME = 'hyphen'

    def simple_check(self, document):
        for word in document.words:
            if '-' in word:
                if word.replace('-', '') in document.words:
                    self.logger.warning(f"using {word} and {word.replace('-', '')}")
