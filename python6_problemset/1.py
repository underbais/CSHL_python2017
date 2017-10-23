#!/usr/bin/env python3

import re

with open("Python_06_nobody.txt", "r") as nobody:
	for line_num,line in enumerate(nobody):
		line = line.rstrip()
		for match in re.finditer(r"Nobody", line):
			print("Number of matching line:",line_num+1,match,'Start:',match.start(), 'End',match.end())

	

