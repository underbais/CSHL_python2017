#!/usr/bin/env python3

import re

with open("Python_06.fasta", "r") as fasta:
	for line in fasta:
		line = line.rstrip()
		for match in re.finditer(r"(^>\S+)(\s\w+.*)", line):
			print('Gene ID:',match.group(1), 'Description:', match.group(2))
	

