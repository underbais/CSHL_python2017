#!/usr/bin/env python3


nums = [101,2,15,22,95,33,2,27,72,15,52]

print('The original list:',nums)

nums_pop = nums.pop()
print('Popped value:',nums_pop)
print('The list after popping:',nums)

print('The original list got shrunk\n-------------------------')

print(nums)

nums_remove = nums.remove(101)

print(nums_remove)
print(nums)
print('Remove shrinks the list and removes by value')



	
