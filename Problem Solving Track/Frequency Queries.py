#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    # print(queries)

    freqNumber={}

    responses=[]

    for item in queries:
        operation,value=item[0],item[1]

        # print(operation,value)

        if operation==1:
            freqNumber[value]=freqNumber.get(value,0)+1

        elif operation==2:
            if value in freqNumber and freqNumber[value]!=0:
                freqNumber[value]-=1

        elif operation==3:
            if any(value == y for y in freqNumber.values()):
                responses.append("1")
            else:
                responses.append("0")
            
    
    # print(freqNumber)


    return responses

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
