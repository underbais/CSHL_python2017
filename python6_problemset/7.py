#!/usr/bin/env python3

import re
seq = ''
with open("Python_06_ApoI.fasta", "r") as fasta:
	for line in fasta:
		if not line.startswith('>'):
			line = line.rstrip()
			seq = seq + line

new_seq = re.sub(r"([AG])AAT([CT])",r"\1^AAT\2" ,seq)

print(new_seq)




	
