'''This Problem is SOlvable in 2 ways,Either make all the pairs and add them to the list and
get the new list\n's length or we can simply count the pairs of words.For this first i got
all the indexes where the capital letters area and then add the first and last index.Then subtract
-1 to get the list of pairs.The reason why i subtracted -1 is that if we do not subtract -1,it
returns the count one more than what we need.'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.


def camelcase(s):
    capIndex = [i for i in range(len(s)) if s[i] <= 'Z']

    capIndex.insert(0, 0)
    capIndex.append(len(s))

    # newlist=[]

    # for i in range(len(capIndex)):
    #     try:
    #         newlist.append(s[capIndex[i]:capIndex[i+1]])
    #     except:
    #         pass

    return len(capIndex)-1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
