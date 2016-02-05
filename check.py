#!/usr/bin/python3

"""
Check how your home directory differs from the configuration in this
repository.
"""

import os
import filecmp

FILE_FOUND = "\033[34m[F]\033[0m"
FILE_MISSING = "\033[33m[?]\033[0m"
FILE_MODIFIED = "\033[36m[M]\033[0m"

print("Staus of your home:\n",
      "[F] file found\n",
      "[M] file is modified\n",
      "[?] file missing\n",
     )

target_home = os.path.expanduser('~')
reference_home= './home'

for path, dirs, files in os.walk(reference_home, topdown=True):
    # slice away the reference home location
    target_path = path[len(reference_home)+1:]

    for file in files:
        expected_file = os.path.join(target_home, target_path, file)
        expected_file = os.path.abspath(expected_file)

        if os.path.exists(expected_file):
            repo_file = os.path.join(path, file)
            if filecmp.cmp(expected_file, repo_file):
                print("{0} {1}".format(FILE_FOUND, expected_file))
            else:
                print("{0} {1}".format(FILE_MODIFIED, expected_file))
        else:
            print("{0} {1}".format(FILE_MISSING, expected_file))
