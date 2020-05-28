"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

Could Have Considered A Dictionary Here Since the Search and Insertion is O(1).Would have
been a more efficient solution

"""


from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        status_check = False
        if arr:
            for index, item in enumerate(arr):
                try:
                    test_index = arr.index(item * 2)
                    # I not equal to J and still we have 2 separate elements
                    # If indexes are same then we do not need to consider(Like for Zero Case)
                    if test_index != index:
                        status_check = True
                        break
                except:
                    pass

        return status_check


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op_2 = new_op.checkIfExist(list_input)
print(new_op_2)
