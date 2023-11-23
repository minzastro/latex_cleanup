#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23.11.2023

@author: mints
"""
import re
from latex_cleanup.checks.basic import BasicCheck


class LabelCheck(BasicCheck):
    NAME = 'Label'

    def __init__(self):
        super(LabelCheck, self).__init__()

    def simple_check(self, document):
        labels = set(re.findall(r'\\label\{([\w:]+)\}', ' '.join(document.text)))
        refs = set(re.findall(r'\\\w+ref\{([\w:]+)\}', ' '.join(document.text)))
        for item in refs - labels:
             self.logger.warning("Reference without label: %s" % item)
        for item in labels - refs:
             self.logger.warning("Label without reference: %s" % item)


