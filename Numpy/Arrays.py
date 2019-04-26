import numpy


def arrays(arr):
    # complete this function
    # use numpy.arrayreturn

    # The Double Colon Syntax Here is used to specify the start and end syntax
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
