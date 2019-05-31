from collections import namedtuple

no_of_cases = int(input())
combined_val = input().find("MARKS")
namingtuple = ("Main", "MARKS")

average_val = 0

for _ in range(no_of_cases):
    data = input()[combined_val : combined_val + 2]
    average_val += int(data)

print(round(average_val / no_of_cases, 2))
