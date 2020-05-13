"""
https://www.geeksforgeeks.org/sieve-of-eratosthenes/

Sieve of Erasthonesis implementation. I have done it based on the example only

https://codereview.stackexchange.com/questions/188053/project-euler-problem-7-in-python-10001st-prime-number/188063

Also used this as reference
"""

# number_range = range(2, 114320)

# new_dictionary = {item: "unmarked" for item in number_range}

# # Sieve of Erasthonesis Algorithm (O(N^2))
# for item in number_range:
#     for key in new_dictionary.keys():
#         if key % item == 0 and key >= item ** 2:
#             new_dictionary[key] = "marked"

# final_prime_list = [
#     item for item in new_dictionary.keys() if new_dictionary[item] == "unmarked"
# ]

# print(final_prime_list)


def nth_prime(n):
    counter = 2
    for i in range(3, n ** 2, 2):
        k = 1
        while k * k < i:
            k += 2
            if i % k == 0:
                break
        else:
            counter += 1
        if counter == n:
            return i


print(nth_prime(10001))
