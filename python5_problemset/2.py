#!/usr/bin/env python3

file = open("Python_05.txt", "r")
new_file = open("Python_05_uc.txt", "w")
#content = file.read()
for line in file:
	line = line.upper()
	line = line.rstrip()
	new_file.write(line+"\n")
file.close()
new_file.close()
