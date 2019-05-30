'''re.compile can be used to check if the expression itself is valid.
Returns a pattern object if successfull.Re.error is used to check for errors with
regular expressions

'''

import re

no_of_cases=int(input())

for _ in range(no_of_cases):
    regex=input()

    try:
        re.compile(regex)
        print(True)

    except re.error:
        print(False)

