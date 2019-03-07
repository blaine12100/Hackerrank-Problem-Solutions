'''In this Question,we take the input as the no of cases(can be dynamic) and calculate
the probability as requried.


No of Cases:5(Trials)

Probability of getting a defect(12 %of 10)=1/3
Probability of not getting a defect:1-P of Getting reject=2/3

1'st defect in 5th inspection

so trials is 5,p and q are know  to us

This is a geometric distribution which itself is a special type of negative 
binomial distribution
'''
import math

def geometric(n,p,q):
    failurepower=q**(n-1)

    return p*failurepower

trials=5
psuccess=(1/3)
pfailure=1-psuccess

op=geometric(trials,psuccess,pfailure)

print(round(op,3))