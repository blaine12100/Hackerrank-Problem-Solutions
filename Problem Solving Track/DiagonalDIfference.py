#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    primary_Diagonal=0
    secondary_Diagonal=0

    # print(len(arr),arr)

    for i in range(len(arr)):
        for j in range(len(arr)):

            if (i+j)==(len(arr)-1):
                secondary_Diagonal+=arr[i][j]
                # print(f'Secondary Diagonal is {arr[i][j]} {i}{j}')

            if i==j:
                primary_Diagonal+=arr[i][j]
                # print(f'Primary Diagonal is {arr[i][j]}')

            

    # print(primary_Diagonal,secondary_Diagonal)
    return abs(primary_Diagonal-secondary_Diagonal)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
