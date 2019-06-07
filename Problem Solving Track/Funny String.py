#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):

    reverse_string = s[::-1]

    abs_diff_og = [
        abs(ord(s[x]) - ord(s[x + 1])) for x in range(len(s)) if x != len(s) - 1
    ]

    abs_diff_rev = [
        abs(ord(reverse_string[x]) - ord(reverse_string[x + 1]))
        for x in range(len(s))
        if x != len(s) - 1
    ]

    # print(abs_diff_og, abs_diff_rev)

    if abs_diff_og == abs_diff_rev:
        return "Funny"

    else:
        return "Not Funny"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + "\n")

    fptr.close()
