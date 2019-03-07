'''
In this Question,we need to find the probability of the given problem using 
the poisson distribution.


lambda:Average no of Successes

k:No of Actual Successes

The probabiliy of success is propotional to lambda

probability of success with very small area(lambda) is virtually zero

A random variable,X, follows Poisson distribution with mean of 2.5. 
Find the probability with which the random variable X is equal to 5.

mean=lambda=2.5
here k should be 5.
'''
import math

def poisson(lambda1,k):
    lambda_power_k=lambda1**k
    e_power=2.71828**(-lambda1)

    op=(lambda_power_k*e_power)/math.factorial(k)

    return round(op,3)

lambda1=2.5
k=5

ans=poisson(lambda1,k)
print(ans)
