#!/usr/bin/python3

import os
import glob

file_found = "\033[36m[F]\033[0m"
file_missing = "\033[33m[?]\033[0m"

print("Staus of your home:\n",
	"[?] file missing\n",
	"[F] file found\n",
	"[M] file is modified\n")

repo_files = glob.glob("**", recursive=True)

for f in repo_files:
	expected_file = os.path.join(os.path.expanduser('~'), f)
	if os.path.exists(expected_file):
		print("{0} {1}".format(file_found, expected_file))
	else:
		print("{0} {1}".format(file_missing, expected_file))
