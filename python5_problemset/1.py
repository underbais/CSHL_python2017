#!/usr/bin/env python3

file = open("Python_05.txt", "r")
#content = file.read()
for line in file:
	line = line.upper()
#	line = line.rstrip()
	print(line)
file.close()
