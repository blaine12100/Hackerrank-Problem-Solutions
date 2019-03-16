'''Pearsons Corellation coefficient is a very important fourmula as far as 
Data Science is concerned as it helps us determine if two sets of columns are 
corellated to each other i.e the increase in one leads to an increase in the other value.
This can help us in feature reduction.'''

import math

items = int(input())
arrayX = list(map(float, input().split()))
arrayY = list(map(float, input().split()))


def mean(length, numbers):
    return float(sum(numbers)/length)


'''Function to calculate the Standard Deviation for a set of values'''


def StandardDev(initial_length, list_values):

    meanVal = mean(initial_length, list_values)

    variance = sum((i-meanVal)**2 for i in list_values)/initial_length

    standard_deviation = pow(variance, 0.5)

    return standard_deviation


meanX = mean(items, arrayX)
meanY = mean(items, arrayY)

standardDeviationX = StandardDev(items, arrayX)
standardDeviationY = StandardDev(items, arrayY)

covariance = sum((arrayX[i] - meanX) * (arrayY[i] - meanY)
                 for i in range(items))

pearsonsCoefficient = (covariance) / (items*standardDeviationX*standardDeviationY)

print(round(pearsonsCoefficient, 3))
