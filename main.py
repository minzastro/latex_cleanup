#!/usr/bin/env python3
import sys
import re
import argparse

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


class LaTeXhelper(object):
    def __init__(self, args):
        self.aa_subs = load_aa_substitutes()
        self.us_uk = []
        for line in open('en_us_uk.txt', 'r').readlines():
            self.us_uk.append(line.split())
        self.splitter = re.compile(r'[ .,;:()*]', flags=re.IGNORECASE)
        self.words = set()
        self.args = args

    def search_aa_subs(self, line):
        for re_from, _, _, s_to, comment in self.aa_subs:
            search = re.search(re_from, line)
            if search is not None:
                print(f'Warning, "{search[0]}" used, "{s_to}" recommended, {comment}')

    def apply_aa_subs(self, line):
        for re_from, re_to, _, _, _ in self.aa_subs:
            line = re.sub(re_from, re_to, line, flags=re.IGNORECASE)
        return line

    def process_file(self, filename):
        text = open(filename, 'r').readlines()
        for line in text:
            warr = self.splitter.split(line.strip().lower())
            warr = [s for s in warr if len(s) > 3]
            self.words |= set(warr)
            if self.args.aanda:
                self.search_aa_subs(line)
        for word in self.words:
            if '-' in word:
                if word.replace('-', '') in self.words:
                    print(f"Warning, using {word} and {word.replace('-', '')}")
        for us_word, uk_word in self.us_uk:
            if us_word in self.words and uk_word in self.words:
                print(f"Warning, both {us_word} and {uk_word} are used")


def main():
    parser = argparse.ArgumentParser(description="""
    Tool for age deconvolution with GMM method.
    """, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-aa', '--aanda', action="store_true",
                        default=False,
                        help='Use A&A style recommendations')
    parser.add_argument('otherthings', nargs='*')
    args = parser.parse_args()
    latex = LaTeXhelper(args)
    latex.process_file(args.otherthings[0])
    #parser.add_argument('-o', '--output', type=str, default=None,
    #                    help='Output filename')


if __name__ == '__main__':
    main()
