"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # string_number = "".join(str(x) for x in digits)
        # return list(str(int(string_number) + 1))

        # Better Solution is to calculate the sum and if a remainder exists then propagate it
        remainder = 0
        for index in range(len(digits) - 1, -1, -1):
            if remainder:
                new_sum = digits[index] + remainder
            else:
                new_sum = digits[index] + 1
            remainder = 0
            if new_sum % 10 == 0:
                digits[index] = 0
                remainder = new_sum // 10
            else:
                digits[index] = new_sum
                break
        if remainder > 0:
            digits = [remainder] + digits
        return digits


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op_2 = new_op.plusOne(list_input)
print(new_op_2)
