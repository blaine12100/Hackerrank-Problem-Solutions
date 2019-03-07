'''In this Question,we take the input as the no of cases(can be dynamic) and calculate
the probability as requried.


No of Cases:10(Trials)

Probability of getting a regect(12 %of 10)=1.2
Probability of not getting a reject:1-P of Getting reject=0.2

No more than 2 rejects=At most(max 2 rejects)

from 0 to 2 sum binomial distribution

At least 2 rejects=More than 2 rejects
from 2 to 10 sum binomial distrobution

'''
import math

# casesval = 6

probabilitySUccess = 0.12
probabilityFailure = 1-probabilitySUccess

# value_of_x = 3


def cases(n, x):
    main_factorials = math.factorial(
        n)/(math.factorial(n-x) * math.factorial(x))

    boyPower = probabilitySUccess**x
    girlPower = (probabilityFailure)**(n-x)

    answer = main_factorials*boyPower*girlPower

    return answer


sumvalNoMore = 0
sumValAtleast=0

for i in range(3):
    sumvalNoMore += cases(10, i)

for i in range(2,11):
    sumValAtleast+=cases(10,i)

print(round(sumvalNoMore, 3))
print(round(sumValAtleast, 3))
