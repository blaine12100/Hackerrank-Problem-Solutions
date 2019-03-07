'''
In this Question,we need to find the probability of the given problem using 
the Normal distribution.

we are given the mean and the standard deviation in the question
'''
import math

# meanval=20
# standarddev=2
# variance=standarddev**2

# def normalDistribution(meanval,variance,standarddev,x):
#     expression1=1/(standarddev*math.sqrt((2*3.14)))
#     expression2=((x-meanval)**2)/(2*variance)

#     finalexpression = expression1*(2.71828**(-expression2))

#     return finalexpression

mean, std = 70, 10


def cdf(x):
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round((1-cdf(80))*100, 2))
print(round((1-cdf(60))*100, 2))
print(round((cdf(60))*100, 2))
