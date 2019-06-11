#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):

    migratory_birds = {}

    multi_keys = []

    for item in arr:
        migratory_birds[item] = migratory_birds.get(item, 0) + 1

    max_value = max(migratory_birds.values())

    for key, value in migratory_birds.items():
        if value == max_value:
            multi_keys.append(key)

    return min(multi_keys)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
