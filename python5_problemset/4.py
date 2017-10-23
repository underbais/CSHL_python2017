#!/usr/bin/env python3

lines_num = 0
char_num = 0

with open("Python_05.fastq","r") as fastq_obj:
	for line in fastq_obj:
		print('This line length:', len(line))
		line = line.rstrip()
		lines_num += 1
		char_num = char_num + len(line)
print('total lines:', lines_num)
print('total chars:', char_num)
print('Ave line length:', char_num/lines_num)
