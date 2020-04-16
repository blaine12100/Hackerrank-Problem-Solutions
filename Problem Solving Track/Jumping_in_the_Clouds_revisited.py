#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):

    # Here 3 is used so if it's a thundercloud we need 1 per jump and 2 for thundercloud
    # else for a single jump we need only one level of energy

    return 100 - sum([3 if c[i] == 1 else 1 for i in range(0, n, k)])


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + "\n")

    fptr.close()
