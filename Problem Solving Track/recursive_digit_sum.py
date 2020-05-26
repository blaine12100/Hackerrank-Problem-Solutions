"""
In this question,what we need to do it reduce a number to it's basic digit form
Say if a number is 123
It's basic/super digit is the sum of it's constituent numbers.We are also given a factor
k by which we need to replicate the number(This is done only for the first case)

https://www.sjsu.edu/faculty/watkins/Digitsum00.htm

Alternate Solution:
We can check if the number is a divisible by 9 then the sum of digits is 9 itself
else it is the original number % 9 (Remainder)

For any question when we have to find the sum of digits recursively,we can use this trick
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):

    # Base Condition
    if len(n) == 1 and k == 0:
        return int(n)

    else:

        # Addition and Multiplication share a property where multiplication
        # is equal to repeated addition and we need to do the multiply with K
        # only once.

        initial_digit_sum = sum(int(x) for x in n)

        if k > 0:
            new_str = str(initial_digit_sum * k)
            return superDigit(new_str, 0)

        else:
            new_str = str(initial_digit_sum)
            return superDigit(new_str, 0)


def superDigitAlternative(n, k):

    # Using the Link Mentioned Above
    x = int(n * k) % 9

    return x if x else 9


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigitAlternative(n, k)

    print(result)
    # fptr.write(str(result) + "\n")

    # fptr.close()
