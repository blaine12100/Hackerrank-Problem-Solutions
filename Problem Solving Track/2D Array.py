#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # print(arr)

    store_sums=[]

    for i in range(len(arr)):
        for j in range(len(arr)):

            j_plus1=j+1
            j_plus2=j+2

            i_plus2=i+2
            i_plus1=i+1

            if i_plus2<6 and i_plus1<6 and j_plus1<6 and j_plus2<6:
                summVal=(arr[i][j]+arr[i][j_plus1]+arr[i][j_plus2])+(arr[i_plus1][j_plus1])+(arr[i_plus2][j]+arr[i_plus2][j_plus1]+arr[i_plus2][j_plus2])

                store_sums.append(summVal)
            
    return max(store_sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
