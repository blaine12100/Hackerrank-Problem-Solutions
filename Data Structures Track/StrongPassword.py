'''In this question,the user enters a password and we have to verify 
whether the password is strong or not.The conditions are that the length
of the password should be greater than 6,should have atleast a single lowercase
and uppercase letter along with a digit and a special character.I have done a somewhat simillar
problem and so i used flags as with flags it's easy to check if any single condition gets violated.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.


def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    specialCharequencce = "!@#$%^&*()-+"

    character_count = 0

    length_pwd = len(password)

    numFlag = False
    specialFlag = False
    capitalFlag = False
    lowercaseFlag = False

    for i in password:
        if i.isnumeric():
            numFlag = True

        elif i.isupper():
            capitalFlag = True

        elif i.islower():
            lowercaseFlag = True

        if i in specialCharequencce:
            specialFlag = True

    if numFlag == False:
        character_count += 1

    if capitalFlag == False:
        character_count += 1

    if lowercaseFlag == False:
        character_count += 1

    if specialFlag == False:
        character_count += 1

    return max(character_count, 6-len(password))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
