"""
In this question,we need to find the maximum no of ones which occur in succession.

For this,this is the logic which we are considering.

create an index_set var and a max length var

whenever we see a one,if the index set var is not set set it.

whenever we see a zero,check if the index_set var is set.If yes,then subtract
current index from the index_set and check with max_lenght and reset the index_set

lastly if the index_set var is set but not unset at the end,that means at the end
all we have is our ones.

So here we need to subtract the length of the array-index_set+1 and check with max_set var
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Default Initialization
        index_set, max_length = "!", 0

        for item in range(len(nums)):
            if nums[item] == 1:
                # If we have some numeric value other than our default state then we do not need
                # to do anything
                if index_set != "!":
                    continue
                else:
                    index_set = item

            else:

                # If the element is zero and the index is set to some number other than
                # Our initial State
                if index_set != "!":

                    new_temp_index = item - index_set

                    # Check For Largest Element
                    if new_temp_index > max_length:
                        max_length = new_temp_index

                    index_set = "!"

        # If in the ending sequence we do not get any 0's so this check is needed
        if index_set != "!":

            new_temp_index = len(nums) - index_set

            if new_temp_index > max_length:
                max_length = new_temp_index
                index_set = 0

        return max_length


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
op = new_op.findMaxConsecutiveOnes(list_input)
print(op)
