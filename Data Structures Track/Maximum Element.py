# Enter your code here. Read input from STDIN. Print output to STDOUT
max_no = 0
max_elem_stack = []

no_cases = int(input())

for _ in range(no_cases):
    operation = input().split()

    if operation[0] == "1":
        max_elem_stack.append(int(operation[1]))

        if int(operation[1]) > max_no:
            max_no = int(operation[1])

    elif operation[0] == "2":
        popped_element = max_elem_stack.pop()

        if popped_element == max_no:
            if len(max_elem_stack) > 0:
                max_no = max(max_elem_stack)

            else:
                max_no = 0

    elif operation[0] == "3":
        print(max_no)
