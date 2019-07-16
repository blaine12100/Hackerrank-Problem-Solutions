import re

expression = "^[789]\d{9}$"

no_of_cases = int(input())

for _ in range(no_of_cases):
    user_string = input()

    matches = re.fullmatch(expression, user_string)

    # Empty array check

    if matches:
        print("YES")
    else:
        print("NO")
