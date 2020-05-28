"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of all the numbers to the left of the index is equal to the sum of all the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should return the left-most pivot index.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to the right of index 3.
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.

Takeaway:Try more cases with negative integers and did not expect the question to have an
edge case with the left sub array with empty values.

Another Takeaway is that if brute force works,good that you were able to find a solution for this
see if you can solve it in a better way.

"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Base Condition to Avoid Erroneous Cases
        if nums and len(nums) >= 3:
            # So Here we need to Consider the left sub array could be empty and then the right
            # Sub array could have the sum etc
            for index in range(len(nums)):
                left_sequence = nums[:index]
                right_sequence = nums[index + 1 :]

                if sum(left_sequence) == sum(right_sequence):
                    return index
        return -1

        # Alternate Solution

        total_sum = sum(nums)
        left_sum = 0

        for index, item in enumerate(nums):
            if left_sum == (total_sum - left_sum - item):
                return index
            left_sum += item
        return -1


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op_2 = new_op.pivotIndex(list_input)
print(new_op_2)
