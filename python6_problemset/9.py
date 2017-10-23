#!/usr/bin/env python3

import re
seq = ''
with open("Python_06_ApoI.fasta", "r") as fasta:
	for line in fasta:
		if not line.startswith('>'):
			line = line.rstrip()
			seq = seq + line

new_seq = re.sub(r"([AG])AAT([CT])",r"\1^AAT\2" ,seq)

digest = new_seq.split("^")

digest.sort(key=len, reverse=True)

print(digest)

for pos,band in enumerate(digest):
	print('Position:', pos+1, 'Fragment:',band)




	
