#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    init_a_count=s.count('a')

    len_string=len(s)

    no_of_strings_appended=n//len_string

    substring_a_count=s[:n%len_string].count('a')
    
    return (init_a_count)*(no_of_strings_appended)+substring_a_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
