first_case = int(input())

first_set = set(input().split())

second_case = int(input())

second_set = set(input().split())

# Both Solutions Work(Elements in second set which are not in the first set)

# print(len(first_set.difference(second_set)))
print(len(first_set - second_set))
