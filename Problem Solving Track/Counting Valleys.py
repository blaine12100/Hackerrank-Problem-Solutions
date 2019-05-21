'''This question is a little difficult since the meaning of the valleys and 
everything is not clear.I was initialy trying to count the no of times the 
string DU comes in our Strings(Down and Up represent one valley).Then i 
tried to think about this problem in terms of +1 and -1 representing the 
deviation above or below the sea level.Then i was able to formulate the problem
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley_count=0
    level_count=0

    for i in s:
        # print(i)
        if i=='U':
            level_count+=1
            # print(level_count)
        elif i=='D' :
            level_count-=1
            # print(level_count)

        if level_count==0 and i=='U':
            valley_count+=1

    return valley_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
