'''The Key to this problem is finding out if there is an easy way to find the nearest multiple
of a number from a given number.After Some time,i thought that there could be some mathematical
relation for this.Once i got that,the rest of the problem is very simple.'''

#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#


def gradingStudents(grades):
    #
    # Write your code here.
    #

    list_return = []

    for i in grades:
        above_no = (i - i % 5)+5

        print(above_no)
        diff2 = above_no-i

        if i < 38:
            list_return.append(i)

        elif diff2 < 3:
            list_return.append(above_no)

        else:
            list_return.append(i)

    return list_return


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
