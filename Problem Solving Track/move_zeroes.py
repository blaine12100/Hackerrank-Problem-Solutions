from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Find All Index where we have zero present and then create a new array and add to existing arr
        # We cannot make a copy of the initial array but we can create a new one :-'
        zero_index_arr = []

        for item in range(len(nums)):
            if nums[item] == 0:
                zero_index_arr.append(item)

        for item in zero_index_arr:
            del nums[item]

        nums.extend([0] * len(zero_index_arr))
        print(nums)
        return nums


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op_2 = new_op.moveZeroes(list_input)
print(new_op_2)
