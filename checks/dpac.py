import re
from latex_cleanup.checks.basic import BasicCheck

"""
DPAC Gaia DR4 online documentation guidelines.
"""


class DPACCheck(BasicCheck):
    NAME = 'DPAC'

    MACRO = {'Gaia': '\\gaia',
             'DR4': '\\gdr{4}',
             'FPR': '\\fpr'}

    def __init__(self):
        super(DPACCheck, self).__init__()

    def simple_check(self, document):
        for word, macro in self.MACRO.items():
            if word.lower() in document.words:
                self.logger.warning(f'{word} used, use {macro} instead')

