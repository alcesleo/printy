#!/usr/bin/env python3

"""
Prints all contents of files in a directory to code-fenced markdown!
To put it in a file do ./printy.py directory > hello.md

Requires docopt to be installed.

Usage:
    printy.py <directory>

"""

import sys, os, re, fnmatch
from textwrap import indent
from docopt import docopt

# TODO: as params
excludes = ['.git', '*.sublime-*', '*.md']
# transform glob patterns to regular expressions
excludes = r'|'.join([fnmatch.translate(x) for x in excludes]) or r'$.'

def printify(directory):
    """
    Prints contents of all files in a directory to stdout in
    simple markdown format. Every file gets a heading with its
    filename, and all content is indented as markdown code blocks.
    """

    # output header
    print('# {0}\n'.format(directory))

    # recurse the directory
    for root, dirs, files in os.walk(directory, topdown=True):

        # exclude dirs and files
        dirs[:] = [d for d in dirs if not re.match(excludes, d)]
        files = [f for f in files if not re.match(excludes, f)]

        for filename in files:
            path = os.path.join(root, filename)

            # print file with header
            print('## {0}\n'.format(path))
            with open(path, 'r') as f:
                text = f.read()
                # indent non-empty lines with 4 spaces
                print(indent(text, '    ', lambda line: True))


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')

    printify(args['<directory>'])
