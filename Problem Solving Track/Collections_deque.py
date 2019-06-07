from collections import deque


new_double_queue = deque()

no_cases = int(input())

for _ in range(no_cases):
    before, value, after = input().rpartition(" ")

    if before == "":
        op_string = f"new_double_queue.{after}()"

    else:
        op_string = f"new_double_queue.{before}({after})"
    eval(op_string)

print(*new_double_queue)

