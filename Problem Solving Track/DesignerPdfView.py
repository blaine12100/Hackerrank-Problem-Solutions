"""Given a list of numbers which represent the english alphabet,determine the max
value of the box to be" shown for the given input.For example,if the list of words has abc in it
and the values are a=4 b=10 ,c=5 then the area req is 10*3 as b has the max value in this
sequence and the length of the input is 3.

Could solve this question in a better manner but the brain stopped working :-)
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the designerPdfViewer function below.


def designerPdfViewer(h, word):
    sample_dict = {"a": h[0], "b": h[1], "c": h[2], "d": h[3], "e": h[4], "f": h[5], "g": h[6], "h": h[7], "i": h[8], "j": h[9], "k": h[10], "l": h[11], "m": h[12],
                   "n": h[13], "o": h[14], "p": h[15], "q": h[16], "r": h[17], "s": h[18], "t": h[19], "u": h[20], "v": h[21], "w": h[22], "x": h[23], "y": h[24], "z": h[25]}
    unique_chars = set(word)
    item_values = []
    resutl = 0

    for i in unique_chars:
        item_values.append(sample_dict[i])

    resutl = max(item_values)*len(word)
    # print(resutl)

    return resutl


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
