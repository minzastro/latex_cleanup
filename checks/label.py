#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 23.11.2023

@author: mints
"""
import re
from latex_cleanup.checks.basic import BasicCheck

"""
Check for unreferenced labels and references to
missing labels.
"""
class LabelCheck(BasicCheck):
    NAME = 'Label'

    def __init__(self):
        super(LabelCheck, self).__init__()

    def simple_check(self, document):
        labels = set(re.findall(r'\\label\{([\w:]+)\}', ' '.join(document.text)))
        refs = set(re.findall(r'\\\w*ref\{([\w:]+)\}', ' '.join(document.text)))
        for item in refs - labels:
             self.logger.error("Reference without label: %s" % item)
        for item in labels - refs:
             self.logger.warning("Label without reference: %s" % item)


