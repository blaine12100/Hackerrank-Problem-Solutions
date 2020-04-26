"""
In this problem,we need to get the sum of all even valued terms in the
fibonacci series below 4 million.

So here we will generate the sequence of terms and only add to the sum
if the no is even
"""


first_term, second_term, third_term = 0, 1, 0
n, sum_even = 0, 0

while third_term < 4000000:
    third_term = first_term + second_term
    first_term = second_term
    second_term = third_term
    if third_term % 2 == 0:
        sum_even += third_term
    # n += 1

print(f"The Final Sum is {sum_even} ")
