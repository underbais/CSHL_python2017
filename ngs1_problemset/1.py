#!/usr/bin/env python3

import re
import numpy as np

lines = 0
seq_lengths = []
phreds = []

with open("pfb.fastq", "r") as fastq:
	for index,line in enumerate(fastq):
		lines += 1
		if index%4==1:
			line = line.rstrip("\n")
			seq_lengths.append(len(line))
		if index%4==3:
			line = line.rstrip("\n")
			for base in line:
				phreds.append(ord(base))							
print("Total number of reads:",int(lines/4)) 
print("Avg length is:",int(np.mean(seq_lengths)))
print("SD is:",np.std(seq_lengths))
print("Avg phred is:",np.mean(phreds), 'Std of phred scores:',np.std(phreds))
