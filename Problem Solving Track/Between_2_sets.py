#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    set_factors = set()
    set_factors.update(a)
    set_factors.update(b)
    # print(set_factors)
    factor_count = 0
    for item in a:
        for item2 in b:
            # print(item2, item, item2 % item)
            if item2 % item == 0:
                set_factors.add(item2 // item)

            elif item % item2 == 0:
                set_factors.add(item // item2)

    print(set_factors)

    # For getting common factors(Above solution is somewhat bruteforcy and does not work for some
    # cases) So between numbers would only be the ones which are not present in the array I.e
    # the numbers greater than the max of first and lesser than the min(Since all other numbers)
    # are lready present.

    for item1 in (max(a), min(b) + 1):
        if all(item1 % item2 == 0 for item2 in a) and (
            all(item3 % item1 == 0 for item3 in b)
        ):
            factor_count += 1

    print(factor_count)


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)
