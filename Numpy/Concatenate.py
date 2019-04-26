import numpy

n, m, p = map(int, input().split())

final_list = []
final_list2 = []

for _ in range(n):
    inputvalues = [int(x) for x in input().split()]
    final_list.append(inputvalues)

for _ in range(m):
    inputvalues = [int(x) for x in input().split()]
    final_list2.append(inputvalues)

# print(numpy.concatenate((numpy.array(final_list),numpy.array(final_list2)),axis=0))
print(numpy.vstack((numpy.array(final_list), numpy.array(final_list2))))

'''Can also solve this problem using vstack(Vertical Stack) Which Concatenates the data
based on row wise stacking'''
