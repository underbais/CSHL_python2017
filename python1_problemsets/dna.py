#!/usr/bin/env python3

import sys

codon = sys.argv[1]

dna = 'GTACCTTGATTTCGTATTCTGAGAGGCTGCTGCTTAGCGGTAGCCCCTTGGTTTCCGTGGCAACGGAAAA'

if codon in dna:
   print("Found", codon, "in the DNA sequence")
else: 
   print("Your codon not found")


