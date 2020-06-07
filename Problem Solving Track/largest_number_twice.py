"""
Largest Number At Least Twice of Others

In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.

 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.

Takeaway:
Try Brute Force First. If it works then no Issue and then go for more optimized/less code
solution

"""

from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_element = max(nums)
        max_index = nums.index(max_element)

        # I did not try the earlier solution since i thought this will be too naive solution so hence I tried
        # The below solution
        # if all(x * 2 <= max_element for x in nums[:max_index] + nums[max_index + 1 :]):
        #     return max_index
        # return -1

        # This one is Better Since Although we are making 2 pass
        # Our Return Condition is smaller so the loop in worst case will
        # run only to the end of the list

        for item in nums:
            if item != max_element and max_element < item * 2:
                return -1

        return max_index


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op_2 = new_op.dominantIndex(list_input)
print(new_op_2)
