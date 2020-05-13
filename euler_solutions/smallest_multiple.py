"""
To learn about Euclid's GCD algorithm and to see hwo to use LCM to solve this problem use
https://www.geeksforgeeks.org/smallest-number-divisible-first-n-numbers/
"""


def gcd(a, b):

    if b == 0:
        return a

    else:
        return gcd(b, a % b)


numbers_range = range(1, 21)

print(" ".join(str(x) for x in numbers_range))

initial_ans = 1

for item in numbers_range:
    initial_ans = initial_ans * item // gcd(initial_ans, item)

print(initial_ans)
