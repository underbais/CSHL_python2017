#!/usr/bin/env python3


nums = [101,2,15,22,95,33,2,27,72,15,52]

nums.sort()

for num in nums:
	print(num)

even = [num for num in nums if num%2==0]
odd = [num for num in nums if num%2!=0]

print('The sum of evens:',sum(even))
print('The sum of odds:',sum(odd))


	
