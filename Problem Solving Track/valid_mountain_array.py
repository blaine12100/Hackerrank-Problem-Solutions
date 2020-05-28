"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

    A.length >= 3
    There exists some i with 0 < i < A.length - 1 such that:
        A[0] < A[1] < ... A[i-1] < A[i]
        A[i] > A[i+1] > ... > A[A.length - 1]

Takeaway:Wrote Code Mostly One Shot with Proper Thinking Flow on Paper.
Was unable to think in terms of the edge cases
"""

from typing import List


# Our Original Solution
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        mountain_valid = False
        peak_index = 0
        strictly_increasing_count = 0
        valley_found = 0

        if A and len(A) >= 3:

            for item in range(1, len(A)):
                # Increasing Peak
                if A[item] > A[item - 1]:
                    strictly_increasing_count += 1
                elif A[item - 1] == A[item]:
                    break
                elif strictly_increasing_count >= 1:
                    peak_index = item - 1

                    # Existing One Valley found then we are going for a hill so that's wrong
                    if valley_found:
                        break
                    else:
                        # Decreasing Peak
                        for item in range(peak_index + 1, len(A)):
                            if A[item - 1] > A[item]:
                                mountain_valid = True
                            else:
                                mountain_valid = False
                                break

                    break

                else:
                    valley_found += 1

        return mountain_valid

        # LeetCode Official Solution(Much Simpler and Easier to Understand than my solution :-))
        # N = len(A)
        # i = 0

        # walk up
        # while i + 1 < N and A[i] < A[i + 1]:
        #     i += 1

        # peak can't be first or last
        # if i == 0 or i == N - 1:
        #     return False

        # walk down
        # while i + 1 < N and A[i] > A[i + 1]:
        #     i += 1

        # return i == N - 1


# Driver Code
new_op = Solution()
list_input = list(map(int, input().split()))
new_op_2 = new_op.validMountainArray(list_input)
print(new_op_2)
