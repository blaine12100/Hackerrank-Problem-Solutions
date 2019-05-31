first_case = int(input())

first_set = set(input().split())

second_case = int(input())

second_set = set(input().split())

# Both Solutions Work(Returns a set of uncommon elements which belong to either sets but nt both sets)

# print(len(first_set.symetric_difference(second_set)))
print(len(first_set ^ second_set))
