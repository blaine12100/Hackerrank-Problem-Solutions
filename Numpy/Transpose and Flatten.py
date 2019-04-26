import numpy
import time

'''Since both the operations operate on a new instance of the array,the time taken 
will almost be the same in both the cases'''

n, m = map(int, input().split())

final_list = []

for _ in range(n):
    inputvalues = [int(x) for x in input().split()]
    final_list.append(inputvalues)

print(numpy.array(final_list).T)
print(numpy.array(final_list).flatten())
