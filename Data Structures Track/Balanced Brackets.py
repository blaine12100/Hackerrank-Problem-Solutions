#!/bin/python3

import math

import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):

    string_stack = []

    for item in s:
        if len(string_stack) == 0:
            string_stack.append(item)

        else:
            if (
                (string_stack[-1] == "(" and item == ")")
                or (string_stack[-1] == "{" and item == "}")
                or (string_stack[-1] == "[" and item == "]")
            ):
                string_stack.pop()

            else:
                string_stack.append(item)

    if string_stack:
        return "NO"

    else:
        return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)

        fptr.write(result + "\n")

    fptr.close()
