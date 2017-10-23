#!/usr/bin/env python3
seq = ''
with open("Python_05.fasta", "r") as file:

	for line in file:
		if line.startswith(">"):
			if seq:
				seq = seq[::-1]
				print(seq)
				seq = ''
			print(line, end='')
			
				
		else:
			line = line.rstrip()

			line = line.replace('A','t')
			line = line.replace('T','a')
			line = line.replace('C','g')
			line = line.replace('G','c')
			line = line.upper()
			seq = seq + line


#			print(line)
seq = seq[::-1]
print(seq)
file.close()
