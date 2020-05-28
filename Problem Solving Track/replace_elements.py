"""
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
After doing so, return the array.

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]

Takeaway : Keep solution simple and not to overcomplicate the solution
"""
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Non Empty Case
        if arr:
            for item in range(len(arr) - 1):
                # Get Max Element from the Elements to the right of the element(This is right now inefficient
                # As repeated searches will also take place and this is a O(n) operation)
                current_max = max(arr[item + 1 :])
                # Assign Current Element as the Maximum
                arr[item] = current_max
                pass

            arr[-1] = -1
        return arr


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op_2 = new_op.replaceElements(list_input)
print(new_op_2)
