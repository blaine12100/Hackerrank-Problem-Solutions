import numpy as np

n, m = map(int, input().split())

'''This Allows us to create 2 arrays with variable inputs to perform our arithmetic operations'''

array1, array2 = (np.array([input().split()
                            for _ in range(n)], dtype=int) for _ in range(2))

print(array1+array2)
print(array1-array2)
print(array1*array2)
print(array1//array2)
print(array1 % array2)
print(array1**array2)
