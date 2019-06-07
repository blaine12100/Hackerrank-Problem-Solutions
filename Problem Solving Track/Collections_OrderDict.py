from collections import OrderedDict

item_dictionary = OrderedDict()

no_of_cases = int(input())

for _ in range(no_of_cases):
    item = input().split()

    item_name = " ".join(str(item[e]) for e in range(0, len(item) - 1))

    # print(item[-1])

    item_value = int(item[-1])

    if item_name in item_dictionary:
        item_dictionary[item_name] += item_value

    else:
        item_dictionary[item_name] = item_value

for key, value in item_dictionary.items():
    print(f"{key} {value}")

