import numpy

shape_input = list(map(int, input().split()))

# print(shape_input)
print(numpy.zeros(shape_input, dtype=numpy.int))
print(numpy.ones(shape_input, dtype=numpy.int))
