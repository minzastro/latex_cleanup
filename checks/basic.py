#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 12:00:57 2017

@author: mints
"""
import logging
import os
import json


class BasicCheck(object):
    NAME = 'basic'

    def __init__(self):
        self.logger = logging.getLogger(self.NAME)
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '%(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(handler)
        self.config = self.load_config()

    def load_config(self):
        conf_name = '%s.conf' % __file__[:-3]
        if os.path.exists(conf_name):
            return json.load(open(conf_name))
        else:
            return {}
            
    def simple_check(self, document):
        raise NotImplemented

    def latex_check(self, document):
        return document.out_text
