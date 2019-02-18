'''In this Question,we need to find the difference between the max hurdle that 
the character can cross and the initial height which he can jump.If the initial height
is greater than his maximum,no need to do the subtraction just return 0 else calculate the 
difference and return it.'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hurdleRace function below.


def hurdleRace(k, height):
    maxHeight = max(height)

    if k > maxHeight:
        return 0
    else:
        drink = maxHeight-k
        return drink


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)

    fptr.write(str(result) + '\n')

    fptr.close()
