"""This file contains a small primer about lambda function,map filter and reduce functions"""


"""Map Function:This function is used to apply a function to a iterable.Could be as simple as
converting every item in an iterable to a particular type or applying a lambda function as a function"""

from functools import reduce

sample_list = ["1", "2", "3", "4", "10", "100", "1000", "23", "43"]

# Using the Len function to calculate the length of every item
new_output = list(map(len, sample_list))

"""Using a lambda function to calculate the Cube of every item.The list is used to convert the 
Result of a generator expression to a list for our use"""

other_map = list(map(lambda x: pow(int(x), 3), sample_list))

print(new_output)

sample_list = 2

print(sample_list, type(sample_list))

"""The variable reassignment works as expected.Was asked a question like this.For checking the 
type of the variable,we can use the isinstance or the type argument"""

if isinstance(sample_list, list):

    for item in sample_list:
        print(item)
else:
    print(f"The type of sample_list is {type(sample_list)}")


###################################################################################

"""Filter Function

The filter function works a little different from the map function as it is normally used
to filter values from a given iterable given a function to evaluate the iterable.Say from our
iterable,we need to get values which  are greater than 1000.In this case,we can use a lambda
function to check for values which are greater than 1000.It returns values which are true
"""

sample_list = ["1", "2", "3", "4", "10", "100", "1000", "23", "43"]

filter_output = list(filter(lambda x: int(x) >= 100, sample_list))

print(filter_output, type(sample_list))

####################################################################################

"""Reduce Function

The reduce function is simillar to the map function in the sense that it needs 2 arguments
A function and an iterable.The difference is that it uses the output of the previous computation
to use as the next input variable.Hence reduce is used for performing mathematical operations on
a iterable.Like say getting the sum,product of entire arrays etc,It returns a single value and 
if we try to covnert it to a list,it gives an error saying that an integer cannot be converted 
to a list
"""

reduce_output = reduce(lambda x, y: int(x) + int(y), sample_list)

print(reduce_output)

####################################################################################
