'''The questions requires us to perform a left rotation which means to shif the output 
by one to the left.If the array is [1,2,3] and we have to perform a single rotaions,the 
array becomes [2,3,1]

For right rotation the same input becomes [3,1,2]
'''

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    for i in range(d):
        _op = a.pop(0)
        a.append(_op)

    print(" ".join(str(c) for c in a))
