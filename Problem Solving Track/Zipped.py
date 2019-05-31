"""
* is used to unpack multiple corresponding elements from each list.Also,good question to work using
zipped module to combine several values into a single value

"""

no_of_items, no_of_cases = map(int, input().split())

iniital_numbers = [list(map(float, input().split())) for _ in range(no_of_cases)]

collected_values = list(zip(*iniital_numbers))

for item in collected_values:
    print(round(sum(item) / len(item), 1))
