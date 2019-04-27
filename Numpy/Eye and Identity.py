import numpy

#Add Spaces to the print output(numpy Version Number)
'''
The Eye Function is the same as the identity function in the default case(K=0)
as it allows us to print the sequence of ones for the main diagonal,lower diagonal and
upper diagonal.The identity function returns the identity matrix for a nxn matrix(n
is the parameter)
'''
numpy.set_printoptions(legacy='1.13')
rows, columns = map(int, input().split())

print(numpy.eye(rows, columns, k=0))
