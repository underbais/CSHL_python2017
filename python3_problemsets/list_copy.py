#!/usr/bin/env python3

my_list = ['a','bb','ccc']
list_copy = my_list
list_copy.append('dddd')
print('This is copy by assignment',list_copy)

my_list = ['a','bb','ccc']
list_copy = my_list.copy()
list_copy.append('dddd')
print('This is copy by .copy method', list_copy)

