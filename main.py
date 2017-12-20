#!/usr/bin/env python3
import argparse
from glob import glob
import importlib
from latex_cleanup.loader import LaTeXloader


def main():
    parser = argparse.ArgumentParser(description="""
    Tool for age deconvolution with GMM method.
    """, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-c', '--check', type=str, default=None,
                        help='List of checks to apply (default: all)')
    parser.add_argument('-f', '--full', action="store_true",
                        default=False,
                        help='Run full check, highlight problems in text')
    parser.add_argument('otherthings', nargs='*')
    args = parser.parse_args()
    latex = LaTeXloader(args.otherthings[0])
    checkers = {}
    for file in glob('checks/[a-z]*.py'):
        base_name = file.split('/')[1][:-3]
        p = importlib.import_module(f"checks.{base_name}")
        for key, value in p.__dict__.items():
            if key[0] != '_' and key != 'BasicCheck' and isinstance(value, type):
                checkers[value.NAME] = value
    if args.check is not None:
        checkers = {k: v for k, v in checkers.items() if k in args.check.split(',')}
    for key, _class in checkers.items():
        check = _class()
        if args.full:
            latex.out_text = check.latex_check(latex)
        else:
            check.simple_check(latex)
    if args.full:
        for line in latex.out_text:
            print(line, end='')

if __name__ == '__main__':
    main()
