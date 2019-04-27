# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

'''Space Issues with Format

Floor rounds off values to the nearest integer on the lower side(largest variable <=x) of the variable
Eg if input is 7.7 the value returned by floor would be 6

Ceil does the exact pposite i.e it roudns to the value which is greater than x(smallest value >=x).

Eg if input is 7.7 the value returned by ceil would be 7 since the smalles value greater than 7.7 is 7)

rint The rint tool rounds to the nearest integer of input element-wise.
'''
np.set_printoptions(legacy='1.13')
initial_input = np.array(input().split(), dtype=float)

print(np.floor(initial_input))
print(np.ceil(initial_input))
print(np.rint(initial_input))
