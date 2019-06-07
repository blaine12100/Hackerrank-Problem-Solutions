#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):

    element_count = {}

    for item in arr:
        element_count[item] = element_count.get(item, 0) + 1

    print(element_count.items(), max(element_count.values()))

    max_value = max(element_count.values())

    return abs(len(arr) - max_value)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
