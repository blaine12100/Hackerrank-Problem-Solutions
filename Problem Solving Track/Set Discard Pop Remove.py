"""Since we can trust the input here,we can use eval to evaluate the expression.
Else we can also use the ast.literal_eval()which only evaluates if the expression is
pythonic in nature.

The discard function removes an element from the and if the element is not present,it
does not raise a key error while the remove function does the same.The pop function is used to remove a random element from the list.So this has to be used with caution. 
"""

n = int(input())
s = set(map(int, input().split()))

no_of_cases = int(input())

for _ in range(no_of_cases):
    command = input().split()

    # Command is definitely pop
    if len(command) == 1:
        s.pop()

    else:
        exec_val = f"s.{command[0]}({command[1]})"
        eval(exec_val)

print(sum(s))

