#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:22:45 2017

@author: mints
"""
from latex_cleanup.checks.basic import BasicCheck
import re

def load_aa_substitutes():
    def turn_to_re(s_from, s_to):
        re_from = r'(%s)' % re.sub(r'(\.|\(|\))', r'\\\1', s_from)
        re_to = r'{\color{red}\1}{\color{blue} %s}' % re.sub(r'(\.|\(|\))', r'\\\1', s_to)
        if 'X' in re_from:
            re_from = re_from.replace('X', '([\S]*)')
            re_to = re_to.replace('X', '\\2')
            if 'Y' in re_from:
                re_from = re_from.replace('Y', '([\S]*)')
                re_to = re_to.replace('Y', '\\3')
        return [re_from, re_to]
    substitutes = []
    for line in open('aa_language.tsv', 'r').readlines():
        sline = line.strip().split('\t')
        if len(sline) > 2:
            if ';' in sline[1]:
                for pline in sline[1].split(';'):
                    substitutes.append(turn_to_re(pline.strip(), sline[2]) +
                                       sline[1:])
            else:
                substitutes.append(turn_to_re(*sline[1:3]) + sline[1:])
    return substitutes


class AACheck(BasicCheck):
    NAME = 'AA'

    def __init__(self):
        super(AACheck, self).__init__()
        self.aa_subs = load_aa_substitutes()

    def simple_check(self, document):
        for line in document.text:
            for re_from, _, _, s_to, comment in self.aa_subs:
                search = re.search(re_from, line)
                if search is not None:
                    self.logger.warning(f'"{search[0]}" used, "{s_to}" recommended, {comment}')

    def apply_aa_subs(self, line):
        for re_from, re_to, _, _, _ in self.aa_subs:
            line = re.sub(re_from, re_to, line, flags=re.IGNORECASE)
        return line

