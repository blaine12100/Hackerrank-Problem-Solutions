"""
In this question,we need to square each number and sort the array in ascending order

"""

from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for item in range(len(A)):
            A[item] *= A[item]
            print(A[item])

        return sorted(A)


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
op = new_op.sortedSquares(list_input)
print(op)
