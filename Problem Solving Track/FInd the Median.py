#!/bin/python3

import math
import random
import re
import sys
import os

# Complete the findMedian function below.
def findMedian(arr):

    arr.sort()

    index_element = (len(arr) + 1) // 2

    print(arr, index_element)

    return arr[index_element - 1]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    print(result)

    fptr.write(str(result) + "\n")

    fptr.close()
