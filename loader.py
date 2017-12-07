#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:58:31 2017

@author: mints
"""
import re


class LaTeXloader(object):
    def __init__(self, filename):
        self.splitter = re.compile(r'[ .,;:()*]', flags=re.IGNORECASE)
        self.words = set()
        self.text = open(filename, 'r').readlines()
        self.out_text = self.text
        for line in self.text:
            warr = self.splitter.split(line.strip().lower())
            warr = [s for s in warr if len(s) > 3]
            self.words |= set(warr)
