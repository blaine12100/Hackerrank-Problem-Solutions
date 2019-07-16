import re

pattern = "^[a-zA-Z](\w|_|\.|-)+@[A-Za-z]+\.[A-Za-z]{1,3}$"
no_of_cases = int(input())

for _ in range(no_of_cases):
    user_string = input()

    splitted_string = user_string.split(" ")

    matches = re.fullmatch(pattern, splitted_string[1][1:-1])

    # Empty array check

    if matches:
        print(user_string)

