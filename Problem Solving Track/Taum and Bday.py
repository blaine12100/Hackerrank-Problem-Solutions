#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):

    originalcostblack, originalwhitecost = (b * bc), (w * wc)
    convertedcostblack, convertedcostwhite = (b * (wc + z)), (w * (bc + z))

    min_totalcost = min(originalcostblack, convertedcostblack) + min(
        originalwhitecost, convertedcostwhite
    )

    return min_totalcost


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        bw = input().split()

        b = int(bw[0])

        w = int(bw[1])

        bcWcz = input().split()

        bc = int(bcWcz[0])

        wc = int(bcWcz[1])

        z = int(bcWcz[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + "\n")

    fptr.close()
