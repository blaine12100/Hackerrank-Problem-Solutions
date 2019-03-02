# Enter your code here. Read input from STDIN. Print output to STDOUT

'''Function to calculate the mean(Sum of an Iterable divided by the length of the iterable)'''
def mean(length, numbers):
    return float(sum(numbers)/length)


'''Function to calculate the median(Find the number of inputs given.Sort them in an ascending order.Then if the number of inputs is odd,divide by 2 and get the number at that particular index in the list of numbers.If the  number of inputs are even
then also divide the length y 2 but get the number at that index and the next index
and take their sum and divide by 2.)
'''
def median(length, num):

    num = sorted(num)

    even_odd = length % 2

    if even_odd == 0:
        index = length//2

        summation = (num[index-1]+num[index])/2

        return float(summation)

    else:
        index = length//2

        return float(num[index])


'''Get the Number which occurs the most number of times.If multiple numbers the 
same ammount of time,get the numerically smallest value.Mode reffers to the most
common number in a given list of numbers'''
def mode(numbers):

    count_map = {}

    for i in numbers:
        count_map[i] = count_map.get(i, 0)+1

    # Get max frequency value and get all keys which have the same max value
    max_value = max(count_map.values())

    mode_list = [key for key, value in count_map.items() if value == max_value]

    return min(mode_list)


length_numbers = int(input())

values = list(map(int, input().split()))

mean_value = mean(length_numbers, values)
median_value = median(length_numbers, values)
modeValue = mode(values)

print(mean_value)
print(median_value)
print(modeValue)
