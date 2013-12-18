#!/usr/bin/env python3

"""
Prints all contents of files in a directory to code-fenced markdown!
To put it in a file do ./printy.py directory > hello.md

Requires docopt to be installed.

Usage:
    printy.py <directory>

"""

import sys, os
from textwrap import indent
from docopt import docopt

def printify(directory, excludes=['.git']):
    """
    Prints contents of all files in a directory to stdout in
    simple markdown format. Every file gets a heading with its
    filename, and all content is indented as markdown code blocks.
    """

    # output header
    print('# {0}\n'.format(directory))

    # recurse the directory
    for root, dirs, files in os.walk(directory, topdown=True):

        # remove excludes
        dirs[:] = [d for d in dirs if d not in excludes]
        files = [f for f in files if f not in excludes]

        for filename in files:
            path = os.path.join(root, filename)

            # print file with header
            print('## {0}\n'.format(path))
            with open(path, 'r') as f:
                text = f.read()
                print(indent(text, '    ', lambda line: True)) # indent non-empty lines with 4 spaces


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')

    printify(args['<directory>'])
