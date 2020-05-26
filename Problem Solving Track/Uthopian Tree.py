"""This question is quite simple if you are able to think in terms of odd and
even numbers dentoting the spring and winter cycles respectively.On my first
crack at this problem,i was unable to think in terms of odd and even nos so
it was a little difficult for me."""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    tree_height = 1

    if n == 0:
        return tree_height

    else:
        for i in range(1, n + 1):
            if i % 2 == 0:
                tree_height += 1
                print("Even Case", i)
            else:
                tree_height *= 2
                print("Odd Case", i)

    return tree_height


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        fptr.write(str(result) + "\n")

    fptr.close()
