"""
Given an array nums of integers, return how many of them contain an even number of digits. 

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.

The Logic to Solve this is as follows.

Here what we need to do this take the digits and count one by one how many 
numbers are there in the number

Then this count needs to be checked to see if it is divisible by 2

Other Alternate solution is to use the length module and directly modify the count on the
basis of the length of the str(Converting from an int to str is much simpler) and can be
done in O(n) time
"""

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        number_count = 0
        for item in nums:
            copy_item = item
            digit_count = 0

            while copy_item > 0:
                remainder = copy_item % 10
                digit_count += 1
                copy_item = copy_item // 10

            if digit_count % 2 == 0:
                number_count += 1

        return number_count


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
op = new_op.findNumbers(list_input)
print(op)
