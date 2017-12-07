#!/usr/bin/env python3
import argparse
from glob import glob
import importlib
from latex_cleanup.loader import LaTeXloader

checkers = {}
for file in glob('checks/[a-z]*.py'):
    base_name = file.split('/')[1][:-3]
    p = importlib.import_module(f"checks.{base_name}")
    for key, value in p.__dict__.items():
        if key[0] != '_' and key != 'BasicCheck' and isinstance(value, type):
            checkers[value.NAME] = value


def main():
    parser = argparse.ArgumentParser(description="""
    Tool for age deconvolution with GMM method.
    """, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-aa', '--aanda', action="store_true",
                        default=False,
                        help='Use A&A style recommendations')
    parser.add_argument('otherthings', nargs='*')
    args = parser.parse_args()
    latex = LaTeXloader(args.otherthings[0])
    for key, _class in checkers.items():
        check = _class()
        check.simple_check(latex)


if __name__ == '__main__':
    main()
