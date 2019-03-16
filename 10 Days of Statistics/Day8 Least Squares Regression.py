# Enter your code here. Read input from STDIN. Print output to STDOUT
'''In this,we try to find the value of theta0 and theta1 which is simillar to the 
equeation y=mx+c where m is theta1 and c is theta0.Can reffer to Andrew Ng Machine COurse
for a great explanation for this.Or search for Lienar Regression with a single feature'''

xValues = [95, 85, 80, 70, 60]
yValues = [85, 95, 70, 65, 70]

meanX = sum(xValues)/5
meanY = sum(yValues)/5
sumx = sum(xValues)
sumy = sum(yValues)

sumXsquare = sum(item**2 for item in xValues)
sumXy = sum(x[0]*x[1] for x in zip(xValues, yValues))
numerator = (5*sumXy)-(sumx*sumy)
denominator = (5*sumXsquare)-(sumx**2)

b = numerator/denominator
a = meanY-(b*meanX)
equation = a+(b*80)
print(round(equation, 3))

