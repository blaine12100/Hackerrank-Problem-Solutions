'''In this question,we need to get the count of likes the product ahs received after N days.
They have given out the logic in the questions regarding how the likes and shared count propagate.
Main thing to remember is that we need to keep the track of the people to whom the advert is shared,
then get the count of people who like the advert and add it to the final count'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.


def viralAdvertising(n):
    shared = 0
    liked = 0
    cumulative = 0

    for i in range(n):
        if i == 0:
            shared = 5
            liked = math.floor(5/2)
            cumulative += liked

        else:
            shared = liked*3
            liked = math.floor(shared/2)
            cumulative += liked

    return cumulative


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
