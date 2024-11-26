#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Check for mixing American and UK spellings.
Created on Thu Dec  7 12:35:27 2017

@author: mints
'''
import re
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
                self.logger.warning(f'both {us_word} and {uk_word} are used')
            if self.config['language'] == 'UK' and us_word in document.words:
                self.logger.warning(f'{us_word} used in UK-style document')
            elif self.config['language'] == 'US' and uk_word in document.words:
                self.logger.warning(f'{uk_word} used in US-style document')

    def latex_check(self, document):
        lines = ''.join(document.out_text)
        for us_word, uk_word in self.us_uk:
            if self.config['language'] == 'UK':
                lines = re.sub(r'([^\\\{])\b(%s)\b' % us_word,
                               r'\1{\\color{%s}\2}{\\color{%s} %s}' %
                                   (self.config['color1'],
                                    self.config['color2'],
                                    uk_word),
                               lines, flags=re.I)
            else:
                lines = re.sub(r'([^\\][^\{])\b(%s)\b' % uk_word,
                               r'\1{\\color{%s}\2}{\\color{%s} %s}' %
                                   (self.config['color1'],
                                    self.config['color2'],
                                    us_word),
                               lines, flags=re.I)
        return ['%s\n' % line for line in lines.split('\n')]
