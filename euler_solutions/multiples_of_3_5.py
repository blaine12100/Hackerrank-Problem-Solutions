"""
We need to find all numbers below 1000 which are multiples of 3 or 5 
and add them up together
"""

sum_natural_multiples = sum(x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0)

print(sum_natural_multiples)
