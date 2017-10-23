#!/usr/bin/env python3

seqdict = {}
freqdict = {}
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

for k,v in seqdict.items():
	freqdict = {k:
				{'A':v.count('A'),
				 'C':v.count('C'),
				 'G':v.count('G'),
				 'T':v.count('T')}
 				}
	print('seqName\tA_count\tT_count\tG_count\tC_count\n',k,freqdict[k]['A'],freqdict[k]['T'],freqdict[k]['G'],freqdict[k]['C'])





	
