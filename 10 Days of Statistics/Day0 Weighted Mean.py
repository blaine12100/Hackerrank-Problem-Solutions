# Enter your code here. Read input from STDIN. Print output to STDOUT

'''Function to get the weighted mean of numbers.To find the weighted mean,
multiply the number with it's corresponding weight and divide by the sum
of the total weights.'''
def weightedMean(numbers, weights):

    multiplyTotal = sum(i*j for i, j in zip(numbers, weights))

    return round(multiplyTotal/sum(weights), 1)


no_items = int(input())

numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

weightedmean = weightedMean(numbers, weights)

print(weightedmean)
