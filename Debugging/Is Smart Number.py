'''For This,Had to check the condition for a perfect square and include that
condition too.Once Done,worked Like a Charm.'''

import math


def is_smart_number(num):
    val = int(math.sqrt(num))
    if val**2 == num or num / val == 1:
        return True
    return False


for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
