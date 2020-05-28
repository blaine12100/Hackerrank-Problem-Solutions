from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        initial_length = 0
        for item in range(len(nums)):
            # Non Simillar Element then we copy that element appropriately.
            if nums[item] != val:
                nums[initial_length] = nums[item]
                initial_length += 1

        print(nums)
        return initial_length


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
value_input = int(input())
new_op_2 = new_op.removeElement(list_input, value_input)
print(new_op_2)
