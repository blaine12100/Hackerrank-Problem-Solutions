'''In this question,we need to check how many times does the query string come in the 
main input.If you try to do this in terms of arrays or something,the solution will be difficult and
messy.One of the efficient solutions is to use a Python Dictionary and a List Comprehension'''


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the matchingStrings function below.


def matchingStrings(strings, queries):
    sample_dict = {}
    # Create HashMap of key value pairs

    for i in strings:
        sample_dict[i] = sample_dict.get(i, 0)+1

    sample_dict_keys = sample_dict.keys()

    list_of_values = [sample_dict[key]
                      if key in sample_dict_keys else 0 for key in queries]

    return list_of_values


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
