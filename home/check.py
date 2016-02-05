#!/usr/bin/python3

import os
import glob

file_found = "\033[36m[F]\033[0m"
file_missing = "\033[33m[?]\033[0m"

print("Staus of your home:\n",
	"[?] file missing\n",
	"[F] file found\n",
	"[M] file is modified\n")

for root, dirs, files in os.walk(".", topdown=True):
	for file in files:
		expected_file = os.path.join(os.path.expanduser('~'), root, file)
		expected_file = os.path.abspath(expected_file)
		if os.path.exists(expected_file):
			print("{0} {1}".format(file_found, expected_file))
		else:
			print("{0} {1}".format(file_missing, expected_file))
