#!/usr/bin/env python

import argparse
import curses.ascii
import contextlib

from fontTools.ttLib import TTFont


def chars_in_ttf(ttf):
    with contextlib.closing(ttf):
        tables = ttf['cmap'].tables
    chars = (chr(num)
             for area in tables
             for num in area.cmap.keys())
    for char in chars:
        if curses.ascii.iscntrl(char):
            continue
        yield char


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ttf_files', metavar='N',
                        type=argparse.FileType('rb'),
                        nargs='+',
                        help='Filepath for TTF file.')
    args = parser.parse_args()
    for f in args.ttf_files:
        ttf = TTFont(f)
        for char in chars_in_ttf(ttf):
            print(char, end='')


if __name__ == '__main__':
    main()
