"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # This Solution right now beats 98.9% of solutions in python right now.
        # Need to Think a little more how can we optimize this more in O(n) time
        length_array = len(nums)
        initial_set = set(range(1, length_array + 1))

        uncommon_elements = list(initial_set - set(nums))

        return uncommon_elements


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op.findDisappearedNumbers(list_input)
