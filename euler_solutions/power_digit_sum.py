"""
Problem 16

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?

"""

first_number = 2
power_number = 1000

number_raised = pow(first_number, power_number)

sum_digits = 0

# Seperating each digits to sum them together(Other Possible Methods include
# using reduce and generator expressions.This is more readable and the digit sepe
# rating approach is quite useful for otehr problems too)
while number_raised > 0:
    remainder = number_raised % 10
    number_raised = number_raised // 10
    sum_digits += remainder

print(sum_digits)
