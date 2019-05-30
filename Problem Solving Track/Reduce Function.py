from fractions import Fraction
from functools import reduce

'''Reduce always need a function with 2 arguments.The fractions class is used to 
represent numbers as fractions.Very Convenient Module.

https://www.geeksforgeeks.org/fraction-module-python/

'''

def product(fracs):
    t = reduce(lambda x,y:x*y,fracs)

    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)