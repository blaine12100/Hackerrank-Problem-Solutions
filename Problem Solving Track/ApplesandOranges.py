#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    applecount, orangecount = 0, 0

    appledistances = [x + a if a >= 0 else x - a for x in apples]
    orangedistances = [x + b if b >= 0 else x - b for x in oranges]

    # Apple Count
    for item in range(len(appledistances)):

        if appledistances[item] >= s and appledistances[item] <= t:
            applecount += 1

    # Orange Count
    for index in range(len(orangedistances)):
        if orangedistances[index] >= s and orangedistances[index] <= t:
            orangecount += 1

    print(applecount, orangecount, sep="\n")


if __name__ == "__main__":
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
