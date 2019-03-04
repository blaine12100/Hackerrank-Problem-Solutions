'''Quartiles basically allow allow us to divide our data points and identify the spread 
in our data.

Interquartile range, or IQR: it’s the distance between the first quartile and the third quartile.
The IQR is useful in calculating outliers. Any data value that is more than 1.5 times the IQR away 
from that central 50% group is called an outlier.
'''

def median(length, num):

    num = sorted(num)

    even_odd = length % 2

    if even_odd == 0:
        index = length//2

        summation = (num[index-1]+num[index])/2

        return int(summation)

    else:
        index = length//2

        return int(num[index])


initial_length = int(input())

first_list = list(map(int, input().split(" ")))

MiddleQuartile = median(initial_length, first_list)

'''If The length of the initial array is odd,we don\'t include the middle value(2nd 
quartile in either of the halves.Else we include it)
'''

if initial_length % 2 == 0:

    first_half = [i for i in first_list if i <= MiddleQuartile]
    second_half = [i for i in first_list if i >= MiddleQuartile]

else:

    first_half = [i for i in first_list if i < MiddleQuartile]
    second_half = [i for i in first_list if i > MiddleQuartile]

# print(first_half,second_half)

firstQuartile = median(len(first_half), first_half)
thirdQuartile = median(len(second_half), second_half)

print(firstQuartile, MiddleQuartile, thirdQuartile, sep="\n")

'''Inter Quartile Range:Difference between the third quartile and the first quartile
Helps us to obtain the spread of data for the middle quartile data
'''
