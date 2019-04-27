import numpy

numpy.set_printoptions(legacy='1.13')

n = int(input())

initial_input = list(numpy.array(input().split(), dtype=float)
                     for _ in range(n))

print(numpy.linalg.det(initial_input))
