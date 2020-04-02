"""
In this proble,we have to find the number of k possible pairs which have the character a in them

For this using itertools we compute the K length pairs out of our entire array.

Then using filter we get those pairs which have a in them.

Then we divide the number of pairs which have a and the total number of pairs.
"""

import itertools

len_of_input = int(input())

list_of_inputs = list(map(str, input().split()))

no_of_sequences_to_generate = int(input())

combinations_no_of_sequences = list(
    itertools.combinations(list_of_inputs, no_of_sequences_to_generate)
)

list_of_index_with_a = len(
    list(filter(lambda x: "a" in x, combinations_no_of_sequences))
)

index_count, len_sequence = 0, len(combinations_no_of_sequences)

print(list_of_index_with_a / len_sequence)
