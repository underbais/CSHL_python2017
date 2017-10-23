#!/usr/bin/env python3

import re
seqdict = {}
id = ''

with open("Python_08.fasta", "r") as fasta:
	for line in fasta:
		if line.startswith('>'):
			line = line.rstrip()
			id = line
			seqdict[id] = ''
		elif not line.startswith(">"):
			 line = line.rstrip()
			 seqdict[id] = seqdict[id] + line

for gene,seq in seqdict.items():
	for match in re.finditer(r"ATG(...)*(TAG|TAA|TGA)",seq):
		print(match.group(0))
		print(match)
		






	
