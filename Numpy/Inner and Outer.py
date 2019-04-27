import numpy

first_matirx = numpy.array(input().split(), dtype=int)
second_matirx = numpy.array(input().split(), dtype=int)

# print(first_matirx,second_matirx)

print(numpy.inner(first_matirx, second_matirx))
print(numpy.outer(first_matirx, second_matirx))
