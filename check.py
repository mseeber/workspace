#!/usr/bin/python3

"""
Check if the files $HOME differ from this repo.

Possible states of files in $HOME:

  [F] file found and matches file in repo
  [M] file found but differs from file in repo (modified)
  [S] file is a symlink (this requires attention)
  [?] file missing from $HOME
"""

import os
import filecmp
import argparse
from argparse import RawTextHelpFormatter

FILE_FOUND = "\033[34m[F]\033[0m"      # blue
FILE_MISSING = "\033[33m[?]\033[0m"    # yellow
FILE_MODIFIED = "\033[36m[M]\033[0m"   # cyan
FILE_SYMLINK = "\033[35m[S]\033[0m"    # cyan

parser = argparse.ArgumentParser(description=__doc__,formatter_class=RawTextHelpFormatter)
args = parser.parse_args()

def print_file_state(target_file, reference_file):
    """
    Print an indicator on console on how the target_file differs from
    reference_file.
    """
    if os.path.exists(target_file):
        state = FILE_FOUND

        if not filecmp.cmp(target_file, reference_file):
            state = FILE_MODIFIED

        # symlinks that point to the reference file are evaluated as
        # equal to the reference file, but being a symlink should be
        # reported
        if os.path.islink(target_file):
            state = FILE_SYMLINK
    else:
        state = FILE_MISSING

    print("{0} {1}".format(state, reference_file))


TARGET_HOME = os.path.expanduser('~')
REFERENCE_HOME = './home'

for path, dirs, files in os.walk(REFERENCE_HOME, topdown=True):
    # slice away the reference home location
    target_path = path[len(REFERENCE_HOME)+1:]

    for file in files:
        expected_file = os.path.join(TARGET_HOME, target_path, file)
        expected_file = os.path.abspath(expected_file)
        repo_file = os.path.join(path, file)
        print_file_state(expected_file, repo_file)

