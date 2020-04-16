#!/bin/python3

import math
import os
import random
import re
import sys

"""
In this challenge,we are asked to print the famous staircase pattern with spaces and a particular
character.

Here the basic logic is that for a right alligned staircase,we need to substitute the no of 
spaces based on the no of staircase that we need.

Say for example the staircase is of size = 4. So the first staircase will have the max number of 
spaces(n-1)=3 then the second staircase will have 2 spaces then 1 then zero

At the same time,the number of characters  will increase based on the depth of the staircase
So at the first staircase you will have 1,then at 2nd 2 and so on

For a Left aligned staircase,you only need to do the second loop and ignore the spacing part.

"""

# Complete the staircase function below.
def staircase(n):
    for item in range(1, n + 1):
        # The below part is for printing a right alligned star pattern
        str_pattern = " " * int(n - item) + "#" * item
        # The below part is for printing a left alligned star pattern
        # str_pattern="#"*item
        print(str_pattern)


if __name__ == "__main__":
    n = int(input())

    staircase(n)
