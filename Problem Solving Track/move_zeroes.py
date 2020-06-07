from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # This Algorithm Works For Around 80% of Cases but for casses when
        # we do have a number in middle or a number at the end and all zeroes
        # then in that case swapping directly will not work

        # for item in range(len(nums)):
        #     if nums[item] == 0:
        #         for item2 in range(item + 1, len(nums)):
        #             nums[item2 - 1], nums[item2] = nums[item2], nums[item2 - 1]

        zero_count = nums.count(0)
        nums = [x for x in nums if x != 0]
        nums.extend([0] * zero_count)
        print(nums)


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op.moveZeroes(list_input)
