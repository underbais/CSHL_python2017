#!/usr/bin/env python3

seqs = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

tuples = [(len(seq),seq) for seq in seqs]

for thing in tuples:
	print(thing[0],'\t',thing[1], '\n', sep='')






	
