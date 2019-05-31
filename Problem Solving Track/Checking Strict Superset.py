initial_set = set(map(int, input().split()))

no_of_cases = int(input())

checking_flag = True

for _ in range(no_of_cases):
    checking_set = set(map(int, input().split()))

    if len(checking_set - initial_set) >= 1:
        checking_flag = False
        break

print(checking_flag)

