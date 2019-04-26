import numpy
import time


'''Both Shape and reshape perform the same operation but the shape operation is better
as it modifies the original data while reshape first creates a copy of the data and 
then changes the shape of the data.'''

listinput = list(map(int, input().split()))

a = time.time()
print(numpy.array(listinput).reshape(3, 3))
b = time.time()

print(b-a)

c = time.time()

temp1 = numpy.array(listinput).shape = (3, 3)
print(temp1)
d = time.time()

print(d-c)
