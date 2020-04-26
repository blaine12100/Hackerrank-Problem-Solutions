"""
In this question,we need to get the largest prime factor of a chosen number

https://www.geeksforgeeks.org/prime-factor/
"""

import math

set_prime_factors: set = set()

number = 600851475143

while number % 2 == 0:

    number = number / 2

# To increment in steps of 2(As the number becomes a composite number so we need to divide
# it by every possible number)

for i in range(3, int(math.sqrt(number)) + 1, 2):
    # So Here we keep on dividing the number by i till it is no longer divisible
    # Then we switch the number
    while number % i == 0:
        number = number / i
        set_prime_factors.add(i)

if number > 2:
    set_prime_factors.add(number)

print(max(set_prime_factors))
