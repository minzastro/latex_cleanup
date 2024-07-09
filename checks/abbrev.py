#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Check for unintroduced abbreviation use.
Created on Mon Aug 12 13:21:45 2019

@author: mints
"""
import re
from latex_cleanup.checks.basic import BasicCheck

def count_upper(s):
    return sum(1 for c in s if c.isupper())


class AbbreviationsCheck(BasicCheck):
    NAME = 'Abbreviations'

    def __init__(self):
        self.abbrev = []

    def simple_check(self, document):
        return None

    def latex_check(self, document):
        out_lines = []
        for line in document.out_text:
            out_words = []
            for word in line.split():
                match = re.match(r'([a-zA-Z0-9\-\_]+)\W*', word)
                if match is not None \
                and count_upper(word) > 2 and len(word) >= 3 and all(s not in word for s in "\\.\}\{"):
                    if match.group(1) not in self.abbrev:
                        out_words.append('\\textbf{%s}' % word)
                        self.abbrev.append(match.group(1))
                    else:
                        out_words.append(word)
                    continue
                out_words.append(word)
            out_lines.append(' '.join(out_words) + "\n")
        print('%', self.abbrev)
        return out_lines


