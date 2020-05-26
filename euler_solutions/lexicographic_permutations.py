"""

Lexicographic permutations  
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Takeaway:How to use the the itertools permutation module
"""

from itertools import permutations


def get_millionth(sample_input):
    total_permuatations = list(permutations(sample_input, len(sample_input)))

    return total_permuatations[999999]


input_digits = list(map(int, input().split()))

op = get_millionth(input_digits)
print(op)
