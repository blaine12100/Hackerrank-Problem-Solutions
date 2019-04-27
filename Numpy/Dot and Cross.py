import numpy
n = int(input())

initial_input = list(numpy.array(input().split(), dtype=int) for _ in range(n))

initial_input2 = list(numpy.array(input().split(), dtype=int)
                      for _ in range(n))


'''For matrices,the matrix product refers to the multiplication and summation of corresponding elements
in the first matrix rows and the second amtrix columns(dot product)

the cross product refers to the matrix product with the cosine angle formed between 2 values
'''
print(numpy.dot(numpy.array(initial_input), numpy.array(initial_input2)))
