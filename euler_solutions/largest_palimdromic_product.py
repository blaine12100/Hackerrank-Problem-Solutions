import time

initial_number = 100
final_number = 1000
set_largest = set()
initial_time = time.time()
for item in range(initial_number, final_number):
    for j in range(item + 1, final_number):
        product = str(item * j)
        if product == product[::-1]:
            set_largest.add(int(product))
final_time = time.time()
print(max(set_largest), final_time - initial_time)
