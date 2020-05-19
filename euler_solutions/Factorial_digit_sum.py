"""
Factorial Digit Sum

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""

from functools import reduce

number = 100


def factorial(n):

    if n == 1:
        return n

    return n * factorial(n - 1)


factorial_digits = factorial(number)
sum_digits = reduce(lambda x, y: x + y, [int(x) for x in str(factorial_digits)])
print(sum_digits, factorial_digits)
