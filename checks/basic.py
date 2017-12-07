#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:00:57 2017

@author: mints
"""
import logging


class BasicCheck(object):
    NAME = 'basic'

    def __init__(self):
        self.logger = logging.getLogger(self.NAME)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)

    def simple_check(self, document):
        raise NotImplemented

    def latex_check(self, document):
        return document.out_text