import numpy

n, m = map(int, input().split())

'''To take dynamic input and combine it into a single array with a generator expression'''
initial_input = (numpy.array(input().split(), dtype=int) for _ in range(n))

print(numpy.prod(numpy.sum(initial_input)))
