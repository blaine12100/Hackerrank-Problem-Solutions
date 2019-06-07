#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):

    beautiday = 0

    for item in range(i, j + 1):
        reverse_no = int(str(item)[::-1])

        if abs(item - reverse_no) % k == 0:
            beautiday += 1

    return beautiday


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + "\n")

    fptr.close()
