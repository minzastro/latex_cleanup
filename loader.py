#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 11:58:31 2017

@author: mints
"""
import re


class LaTeXloader:
    def __init__(self, filename):
        self.splitter = re.compile(r'[\\ ._,;:(){}*]', flags=re.IGNORECASE)
        self.words = set()
        self.text = open(filename, 'r').readlines()
        self.out_text = self.text
        for line in self.text:
            warr = self.splitter.split(re.sub('["\'`]', '', line.strip().lower()))
            warr = [s for s in warr if len(s) >= 3 and not re.fullmatch(r'[0-9\.]*', s)]
            self.words |= set(warr)
