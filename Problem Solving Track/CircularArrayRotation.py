"""Given a List of integers,perform a right arary rotaion(A rotaion in which we move
elements to the right i.e last element is inserted at the first position and all 
elements move by one to the right)"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.


def circularArrayRotation(a, k, queries):
    for i in range(k):
        popped = a.pop(-1)
        a.insert(0, popped)

    return [a[i] for i in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
