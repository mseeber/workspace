#!/usr/bin/python3

"""
Check how your home directory differs from the configuration in this
repository.
"""

import os
import filecmp

FILE_FOUND = "\033[34m[F]\033[0m"      # blue
FILE_MISSING = "\033[33m[?]\033[0m"    # yellow
FILE_MODIFIED = "\033[36m[M]\033[0m"   # cyan
FILE_SYMLINK = "\033[35m[S]\033[0m"    # cyan

def print_file_state(target_file, reference_file):
    """
    Print an indicator on console on how the target_file differs from
    reference_file.
    """
    if os.path.exists(target_file):
        if filecmp.cmp(target_file, reference_file):
            state = FILE_FOUND
        else:
            state = FILE_MODIFIED
    else:
        state = FILE_MISSING

    print("{0} {1}".format(state, reference_file))

print("Staus of your home:\n",
      "[F] file found\n",
      "[M] file is modified\n",
      "[S] file is symlink\n",
      "[?] file missing\n",
     )


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

