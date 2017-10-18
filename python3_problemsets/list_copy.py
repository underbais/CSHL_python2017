#!/usr/bin/env python3

# wrong way of creating the copy of a list

my_list = ['a','bb','ccc']
list_copy = my_list # doing this you link them and if copy is modified the original will be modified too!!!
list_copy.append('dddd')
print('This is the original list', my_list)
print('This is a modified copy by assignment',list_copy)

# correct way of doing that

my_list = ['a','bb','ccc']
list_copy = my_list.copy()
list_copy.append('dddd')
print('This is the original list', my_list)
print('This is a modified copy by .copy method', list_copy)

