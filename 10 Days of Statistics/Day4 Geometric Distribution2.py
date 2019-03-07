'''In this Question,we take the input as the no of cases(can be dynamic) and calculate
the probability as requried.


Probability of Success)=1/3
Probability of not getting a reject:1-P of Getting reject=2/3

Found in first 5 inspections.That means x will go from 1 to 6(for 5 in python)

from 1 to 6 sum geometric distribution
'''
import math

probabilitySUccess = 1/3
probabilityFailure = 1-probabilitySUccess

def geometric(n, p, q):
    failurepower = q**(n-1)

    return p*failurepower


sumvalNoMore = 0
for i in range(1, 6):
    sumvalNoMore += geometric(i, probabilitySUccess, probabilityFailure)

print(round(sumvalNoMore, 3))
