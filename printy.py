#!/usr/bin/env python3

"""
Prints all contents of files in a directory to code-fenced markdown!
To put it in a file do ./printy.py directory > hello.md

Requires docopt to be installed.

Usage:
    printy.py <directory>

"""

import sys, os, mimetypes
from textwrap import indent
from docopt import docopt

# TODO: exclude dir option
# TODO: limit mimetypes

def printify(directory):
    """
    Prints contents of all files in a directory to stdout in
    simple markdown format. Every file gets a heading with its
    filename, and all content is indented as markdown code blocks.
    """

    # recurse the directory
    for root, dirs, files in os.walk(directory):
        for filename in files:
            path = os.path.join(root, filename)

            # print file with header
            print('## {0}\n'.format(path))
            with open(path, 'r') as f:
                text = f.read()
                print(indent(text, '    ', lambda line: True)) # indent non-empty lines with 4 spaces


if __name__ == '__main__':
    args = docopt(__doc__)

    printify(args['<directory>'])
