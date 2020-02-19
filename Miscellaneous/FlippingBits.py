#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):

    # Convert Number from Decimal to Binary
    binary_representaion = "{0:b}".format(n)
    # Flip the Bits using a List Comprehension
    flipped_representation = "".join(
        [str(0) if int(item) else str(1) for item in binary_representaion]
    )
    # Generate the Number of Ones accoriding to the remaining length of numbers
    ones_str = "1" * (32 - len(binary_representaion))
    # Convert from Binary to Decimal
    combined_str = ones_str + flipped_representation

    return int(combined_str, 2)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        fptr.write(str(result) + "\n")

    fptr.close()
