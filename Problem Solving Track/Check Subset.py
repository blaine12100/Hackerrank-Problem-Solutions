"""
The check that we need to do is whether all the elements in the first set are present in the second set.This can be done by checking if the intersection of both the elements returns us the first set or not.Or we can also check by using the all keyword and checking each and every element in set A is a part of Set B

"""

no_of_cases = int(input())

for _ in range(no_of_cases):
    no_elem_first = int(input())
    first_set = set(map(int, input().split()))

    no_elem_second = int(input())

    second_set = set(map(int, input().split()))

    if (first_set & second_set) == first_set:
        print(True)
    else:
        print(False)

