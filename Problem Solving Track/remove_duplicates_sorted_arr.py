from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Initial Base Condition
        if not nums or len(nums) == 1:
            return len(nums)

        initial_index = 1
        # Atleast we will be having a single unique element since the blank case has been handled
        # At the start
        edited_index = 1

        while initial_index < len(nums):
            # If element is not the same then we stap the element and keep a count of the
            # of the no of times we have changed the element and so we are getting the
            # first iteration of the unique element in front which leads us to having all initial
            # elements in sequence as needed.
            if nums[initial_index - 1] != nums[initial_index]:
                nums[edited_index] = nums[initial_index]
                edited_index += 1
            initial_index += 1
        print(nums)
        return edited_index


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op_2 = new_op.removeDuplicates(list_input)
print(new_op_2)
