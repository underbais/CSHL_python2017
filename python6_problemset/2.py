#!/usr/bin/env python3

import re
german_lady = open("german_lady.txt", "w")
with open("Python_06_nobody.txt", "r") as nobody:
	for line in nobody:
		line = line.rstrip()
		line =  re.sub(r"Nobody", "German lady", line)
		german_lady.write(line + "\n")
german_lady.close()
	

