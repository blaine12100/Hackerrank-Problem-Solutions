"""Since we can trust the input here,we can use eval to evaluate the expression.
Else we can also use the ast.literal_eval()which only evaluates if the expression is
pythonic in nature.We can also use the getattr method 
"""

n = int(input())
s = set(map(int, input().split()))

no_of_cases = int(input())

for _ in range(no_of_cases):
    command = input().split()

    new_set = set(map(int, input().split()))

    exec_val = f"s.{command[0]}({new_set})"
    eval(exec_val)

print(sum(s))

