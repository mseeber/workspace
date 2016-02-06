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

print("Staus of your home:\n",
      "[F] file found\n",
      "[M] file is modified\n",
      "[S] file is symlink\n",
      "[?] file missing\n",
     )

def print_file_state(state, file_name):
    print("{0} {1}".format(state, file_name))

def file_state(expected_file, repo_file):
    if os.path.exists(expected_file):
        if filecmp.cmp(expected_file, repo_file):
            print_file_state(FILE_FOUND, expected_file)
        else:
            print_file_state(FILE_MODIFIED, expected_file)
    else:
        print_file_state(FILE_MISSING, expected_file)

target_home = os.path.expanduser('~')
reference_home= './home'

for path, dirs, files in os.walk(reference_home, topdown=True):
    # slice away the reference home location
    target_path = path[len(reference_home)+1:]

    for file in files:
        expected_file = os.path.join(target_home, target_path, file)
        expected_file = os.path.abspath(expected_file)
        repo_file = os.path.join(path, file)
        file_state(expected_file, repo_file)


