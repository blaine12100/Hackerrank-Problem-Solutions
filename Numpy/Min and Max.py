import numpy

n, m = map(int, input().split())

'''To take dynamic input and combine it into a single array with a generator expression'''

initial_input = list(numpy.array(input().split(), dtype=int) for _ in range(n))

minvalues = numpy.min(numpy.array(initial_input), axis=1)

print(numpy.max(minvalues))
