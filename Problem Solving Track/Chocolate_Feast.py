#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the chocolateFeast function below.(Logic is simple enough.I got lost for a bit)
def chocolateFeast(n, c, m):
    initial_no_of_wrappers = n // c

    total_wrappers = 0

    total_wrappers += initial_no_of_wrappers

    while initial_no_of_wrappers >= m:

        quotient, remainder = divmod(initial_no_of_wrappers, m)

        total_wrappers += quotient

        initial_no_of_wrappers = quotient + remainder

    return total_wrappers


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        ncm = input().split()

        n = int(ncm[0])

        c = int(ncm[1])

        m = int(ncm[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + "\n")

    fptr.close()
