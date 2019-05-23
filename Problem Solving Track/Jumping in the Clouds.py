'''In this question,we need to cehck if it \n's possible to make a 2 step jump.
If it is possible,then we should allow the user to make a 2 step jump if it is safe 
to do so.(Element at that index should be zero).Skip the One index as necessary.
Using a for loop does not allow us to modify the index to be iterated hence using
a for loop'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    min_jumps=0

    length_list=len(c)

    item=0

    while item<(length_list-1):
        if c[item]==0:
            if item+2<length_list and c[item+2]==0:
                item+=2
                min_jumps+=1

            elif item+1<length_list and c[item+1]==0:
                item+=1
                min_jumps+=1
                
    return min_jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
