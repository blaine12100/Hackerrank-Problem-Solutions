"""
Longest Collatz sequence

https://codereview.stackexchange.com/questions/167664/project-euler-14-longest-collatz-sequence-in-python

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

import time

number_range = range(2, 1000000)
longest_length, corresponding_number = 0, 0

initial_time = time.time()

for number in number_range:
    iterating_number = number

    temp_counter = 1

    while iterating_number != 1:
        if iterating_number % 2 == 0:
            iterating_number //= 2

        else:
            iterating_number = (3 * iterating_number) + 1

        temp_counter += 1

    if temp_counter > longest_length:
        longest_length = temp_counter
        corresponding_number = number

final_time = time.time()
print(corresponding_number, longest_length, final_time - initial_time)
