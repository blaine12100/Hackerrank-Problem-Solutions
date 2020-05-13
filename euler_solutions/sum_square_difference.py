number_range = range(1, 101)
sum_individual_squared = sum([item ** 2 for item in number_range])
sum_squared = sum(number_range) ** 2
print(sum_squared - sum_individual_squared)
