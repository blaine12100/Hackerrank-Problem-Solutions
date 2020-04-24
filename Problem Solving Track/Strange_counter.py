#!/bin/python3

import math
import os
import random
import re
import sys

"""
In the current solution,we are running the for loop for the entire duration of the time till the 
time  we get the desired index.This is causing a Time Limit error for the code.Maybe there is a 
way we can directly calculate the value for an index using some formula.
"""

# Complete the strangeCounter function below.
def strangeCounter(t):
    inital_second_value = 3
    copy_second_value = inital_second_value

    final_value = inital_second_value

    for index in range(1, t + 1):
        # print(index, copy_second_value)
        if index == t:
            final_value = copy_second_value
            break

        if copy_second_value == 1:
            copy_second_value = inital_second_value * 2
            inital_second_value = inital_second_value * 2
            continue

        # print(copy_second_value)

        copy_second_value -= 1

    return final_value


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    result = strangeCounter(t)
    print(result)
    fptr.write(str(result) + "\n")

    fptr.close()
