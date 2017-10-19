#!/usr/bin/env python3

import random
from random import randint, random, shuffle, choice

length = 10
DNA=""
for count in range(length):
   DNA+=choice("CGTA")


print(DNA)
type(DNA)
random.choice(DNA)




