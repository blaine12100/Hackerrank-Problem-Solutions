first_case = int(input())

first_set = set(input().split())

second_case = int(input())

second_set = set(input().split())

# Both Solutions Work

# print(len(first_set.intersection(second_set)))
print(len(first_set & second_set))
