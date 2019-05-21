#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    
    last_Answer=0

    main_list=[[] for i in range(n)]

    ret_array=[]

    for item in queries:

        query_type,x,y=item[0],item[1],item[2]

        index=((x ^ last_Answer)%n)

        if query_type==1:
            main_list[index].append(y)

        elif query_type==2:
            seq_length=len(main_list[index])
            seq_item=main_list[index][y%seq_length]

            last_Answer=seq_item

            ret_array.append(last_Answer)


    return ret_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()

    n = int(nq[0])

    q = int(nq[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
