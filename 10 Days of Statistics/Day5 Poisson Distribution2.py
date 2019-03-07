'''In this Question, we need to find the probability of the given problem using
the poisson distribution.


lambda: Average no of Successes
we have been given lambda1 0.88 and lambda2 as 1.55

Cost of a =160+40X^2
Cost of b =128+40y^2

We have to find the cost of running the machine for a single day
'''
def Cost(lambda1,lambda2):
    XSquare=lambda1+lambda1**2
    YSquare=lambda2+lambda2**2

    costA=160+(40*XSquare)
    costB=128+(40*YSquare)

    return round(costA,3),round(costB,3)


cost1,cost2=Cost(0.88,1.55)

print(cost1)
print(cost2)

