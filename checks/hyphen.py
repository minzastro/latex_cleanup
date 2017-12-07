#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:01:57 2017

@author: mints
"""
import re
from latex_cleanup.checks.basic import BasicCheck


class HyphenCheck(BasicCheck):
    NAME = 'hyphen'

    def simple_check(self, document):
        for word in document.words:
            if '-' in word:
                if word.replace('-', '') in document.words:
                    self.logger.warning(f"using {word} and {word.replace('-', '')}")

    def latex_check(self, document):
        warn_words = []
        for word in document.words:
            if '-' in word:
                if word.replace('-', '') in document.words:
                    warn_words.append(r'\b(%s|%s)\b' % (word, word.replace('-', '')))
        cache = []
        for line in document.out_text:
            for w in warn_words:
                cache.append(re.sub(w, r'!!!\1!!!', line))
        return cache