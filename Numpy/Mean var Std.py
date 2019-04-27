import numpy

numpy.set_printoptions(legacy='1.13')
n, m = map(int, input().split())

'''To take dynamic input and combine it into a single array with a generator expression'''

initial_input = list(numpy.array(input().split(), dtype=int) for _ in range(n))

print(numpy.mean(numpy.array(initial_input), axis=1))

print(numpy.var(numpy.array(initial_input), axis=0))

print(numpy.std(numpy.array(initial_input)))
