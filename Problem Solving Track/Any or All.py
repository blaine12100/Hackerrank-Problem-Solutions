no_of_cases = int(input())

str_input = input().split(" ")

print(all(int(i) >= 0 for i in str_input) and any(i == i[::-1] for i in str_input))
