#!/usr/bin/env python3

"""
Usage:
    printy.py <directory>
    printy.py <directory> --exclude=<folder_or_file_pattern>...

Options:
    -h --help     Show this screen.
    --version     Show version.
    --exclude=<glob> Exclude file or folder, for example --exclude='*.pyc'.

"""

import sys, os, re, fnmatch
from textwrap import indent
from docopt import docopt

def _regexify_globs(patterns):
    """Turn a list of glob patterns into a regex."""
    # http://stackoverflow.com/questions/5141437/filtering-os-walk-dirs-and-files
    return r'|'.join([fnmatch.translate(x) for x in patterns]) # to regex


def printify(directory, excludes=None):
    """
    Prints contents of all files in a directory to stdout in
    simple markdown format. Every file gets a heading with its
    filename, and all content is indented as markdown code blocks.
    """

    # standard excludes
    if not excludes:
        excludes = ['.git', '*.sublime-*', '*.md']

    excludes = _regexify_globs(excludes)

    # output header
    print('# {0}\n'.format(directory))

    # recurse the directory
    for root, dirs, files in os.walk(directory, topdown=True):

        # exclude dirs and files
        if excludes:
            dirs[:] = [d for d in dirs if not re.match(excludes, d)]
            files = [f for f in files if not re.match(excludes, f)]

        for filename in files:
            path = os.path.join(root, filename)

            # print file with header
            print('## {0}\n'.format(path))

            # http://docs.python.org/3.3/library/functions.html#open
            with open(path, 'r', errors='ignore') as f:
                # todo ignore binary files
                text = f.read()
                # indent non-empty lines with 4 spaces
                print(indent(text, '    ', lambda line: True))


if __name__ == '__main__':
    args = docopt(__doc__, version='0.1')

    printify(args['<directory>'], args['--exclude'])
