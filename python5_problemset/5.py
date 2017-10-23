#!/usr/bin/env python3

all = open("alpaca_all_genes.tsv", "r")
stem = open("alpaca_stemcellproliferation_genes.tsv", "r")
pigment = open("alpaca_pigmentation_genes.tsv", "r")

all_set = set(line.strip() for line in all)

#for line in all:
#	if not line.startswith('Gene stable ID'):
#		all_set = all_set + set(line.strip()))
	
set_file = open("all_set_file.txt", "w")
set_file.write(all_set)
set_file.close()

print(all_set[0])
