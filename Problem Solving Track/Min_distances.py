#!/bin/python3

import math
import os
import random
import re
import sys

# This solution is basically a bruteforce one and the worst part is, I do not know how to
# optimise this :-(
# Complete the minimumDistances function below.


def minimumDistances(a):
    sample_dict = {}
    max_index_list = set()

    for index, item in enumerate(a):
        for index2, item2 in enumerate(a):
            if item == item2:
                if item in sample_dict:
                    if index2 not in sample_dict[item]:
                        sample_dict[item].append(index2)
                else:
                    sample_dict[item] = [index]

    for value in sample_dict.values():
        if len(value) > 1:
            # Min difference
            for item in value:
                for item2 in value:
                    if item != item2:
                        max_index_list.add(abs(item - item2))

    if len(max_index_list) > 0:
        return min(max_index_list)
    else:
        return -1


if __name__ == "__main__":

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

# 6 7 1 3 4 1 7
