'''In this Question,we take the input as the no of cases(can be dynamic) and calculate
the probability as requried.
'''
import math

# casesval = 6

probabilityBoy = (1.09/2.09)
probabilityGirl = 1-(probabilityBoy)

value_of_x = 3


def cases(n, x):
    main_factorials = math.factorial(
        n)/(math.factorial(n-x) * math.factorial(x))

    boyPower = probabilityBoy**x
    girlPower = (probabilityGirl)**(n-x)

    answer = main_factorials*boyPower*girlPower

    return answer


sumval = 0

for i in range(3, 7):
    sumval += cases(6, i)

print(round(sumval, 3))
