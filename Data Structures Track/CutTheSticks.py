'''This question absically requires you to get the smallest element in the lsit and
subtract the smallest number from all the other elements and remove the elements
which are no longer valid(0).

We can do this in 2 ways,in the first way we create the arr and find the min of the 
arr and subtract that value and filter to remove zero elements.In the other way what we can
do is return the elements which are not equal to the min of the value.

Both the Algorithms are correct and they work'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.


def cutTheSticks(arr):

    given_arr = arr

    new_arr = []

    # Solution one

    while len(given_arr) != 0:
        new_arr.append(len(given_arr))
        min_arr = min(given_arr)
        given_arr = list(
            filter(lambda x: x != 0, [abs(min_arr-i) for i in given_arr]))
        # given_arr=[i for i in given_arr if i!=0]

    #Solution 2

    while given_arr:
        new_arr.append(len(given_arr))
        given_arr = [x for x in given_arr if x != min(given_arr)]

    return new_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
