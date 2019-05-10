'''This is a direct continuation for the least square regression problem but now this is being done with
multiple features instead of a single feature'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model
import numpy
m, n = map(int, input().split())
yvalues = []
xValues = []

for i in range(n):
    rowinput = list(map(float, input().split()))
    xValues.append(rowinput[:m])
    yvalues.append(rowinput[-1])


cases = int(input())
avalue = []
bvalue = []

for i in range(cases):
     rowinput2 = list(map(float, input().split()))
     avalue.append([rowinput2[0], rowinput2[1]])
     bvalue.append(rowinput2[1])


lm = linear_model.LinearRegression()
lm.fit(xValues, yvalues)
a = lm.intercept_
b = lm.coef_
interceptarray = [a, b[0], b[1]]

for i in range(cases):
    newarray = avalue[i]
    newarray.insert(0, 1)
    print(round(numpy.sum(numpy.dot(newarray, interceptarray)), 2))
