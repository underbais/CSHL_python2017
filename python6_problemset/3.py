#!/usr/bin/env python3

import re
with open("Python_06.fasta", "r") as fasta:
	for line in fasta:
		line = line.rstrip()
		if  re.match(r"^>\S\w+", line):
			print(line)
		
	

