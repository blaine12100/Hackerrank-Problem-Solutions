"""

Questions 
1. Write a function that converts an 8-bit signed integer (-128 to 127) to an 8-bit unsigned integer (0 to 255) without any if statements.
"""

"""
2. Write a function that splits a large list into smaller lists of x elements. 
For example, if I have a list of 98 elements and x is 6, I want 17 lists; 16 lists have 6 elements each and my 17th has 2.

large_list = [1,2,3,4,5,6,7,8,9,10, 11, 12 ,13, 14, .................., 98]
output = [[1,2,3,4,5,6],[7,8,9,10,11,12],...[97,98]
"""

# main_list = list(range(99))

# split_list = int(input())

# My Solution

# new_list=[]

# index=split_list

# prev_index=0

# for item in range(1,len(main_list)):
#   new_list.append(main_list[prev_index:index])
#   prev_index+=split_list
#   index+=split_list

#   if index>len(main_list):
#     new_list.append(main_list[prev_index:])
#     break

# print(new_list)

#######################

# https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

# GFG Solution
# def yield_chunks(main_list, split_list):
#     for item in range(0, len(main_list), split_list):
#         yield main_list[item : item + split_list]


# print(list(yield_chunks(main_list, split_list)))

# Using List Comprehension

"""
The item will initially be zero and zero*6 is zero.Then we add +1 to the item so it becomes 1*6=6
So the first slice contains elements from 0:6 
second 6:12
third 12:18 and so on

The last slice will contain all the left over elements which do not confirm to the index margin
"""

# new_list = [
#     main_list[item * split_list : (item + 1) * split_list]
#     for item in range((len(main_list) // split_list) + 1)
# ]

# print(new_list)

# Unsigned to Signed Integer convversion
# (https://stackoverflow.com/questions/385572/typecasting-in-python)

take_input = int(input())

s8 = (take_input + 2 ** 7) % 2 ** 8 - 2 ** 7
unsigned_op = take_input % 2 ** 8

print(unsigned_op)
