'''
Standard Deviation:Helps us in knowing the absolute average distance from the mean

The Variance Meanwhile lets us know the square distance away from the mean.

A low standard deviation means that most of the numbers are very close to the average. 
A high standard deviation means that the numbers are spread out.
'''

def mean(length, numbers):
    return float(sum(numbers)/length)

'''Function to calculate the Standard Deviation for a set of values'''
def StandardDev(initial_length,list_values):

    meanVal=mean(initial_length,list_values)

    variance=sum((i-meanVal)**2 for i in list_values)/initial_length

    standard_deviation=round(pow(variance,0.5),1)

    return standard_deviation


initial_length = int(input())

list_values = list(map(int, input().split()))

standardDeviation=StandardDev(initial_length,list_values)

print(standardDeviation)
