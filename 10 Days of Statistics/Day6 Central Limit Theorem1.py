

import math

mean, std = 205, 15

maxVal=9800

n=49

def cdf(x):
    return 0.5 * (1 + math.erf((x - mudash) / (stddash * (2 ** 0.5))))


mudash=n*mean
stddash=math.sqrt(n)*std

firstCde=cdf(maxVal)

capitalN=firstCde/maxVal
# print(capitalN)
# print(n,capitalN)
# print(n/capitalN)