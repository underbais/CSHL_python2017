#!/usr/bin/env python3

import re
seq = ''
with open("Python_06_ApoI.fasta", "r") as fasta:
	for line in fasta:
		if not line.startswith('>'):
			line = line.rstrip()
			seq = seq + line


for match in re.finditer(r"[AG]AAT[CT]", seq):
	print(match, match.start(), match.end())
	
