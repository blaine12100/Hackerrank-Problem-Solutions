"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.
"""

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        index = 0
        initial_length = len(arr)

        while index < initial_length:
            if arr[index] == 0:
                arr.insert(index + 1, 0)
                del arr[-1]
                index += 2
            else:
                index += 1

        # print(arr)


# Alternate Solution
# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:

#         index = False
#         initial_length = len(arr)

#         for item in range(initial_length - 1):
#             if arr[item] == 0 and not index:
#                 arr[item + 2 :] = arr[item + 1 : -1]
#                 arr[item + 1] =
#                 To skip the next zero inserted
#                 index = True
#             else:
#                 index = False

#         print(arr)


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
op = new_op.duplicateZeros(list_input)
print(op)
