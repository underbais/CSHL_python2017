#!/usr/bin/env python3

import sys

num = float(sys.argv[1])

if num < 0:
   print("It is negative")
elif num == 0:
   print("It equals zero")
elif num > 50:
   print("It is greater than 50")
elif num == 50:
   print("It is exactly 50")
elif num%2==0:
   print("it is a positive number smaller than 50 and it is even")
else:
   print("It is an odd number smaller than 50")
 
    

