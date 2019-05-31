first_case = int(input())

first_set = set(map(int, input().split()))

second_case = int(input())

second_set = set(map(int, input().split()))

# Both Solutions Work(Returns a set of uncommon elements which belong to either sets but nt both sets)

symetric_diff = sorted(list(first_set.symmetric_difference(second_set)))

print(*symetric_diff, sep="\n")

