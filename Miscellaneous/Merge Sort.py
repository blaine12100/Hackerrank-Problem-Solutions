"""
For reference refer to the CLRS book

Q=Middle Index
P=Low
R=High

https://www.geeksforgeeks.org/merge-sort/

The best/worst/average time complexity in this is always O(nlogn) as we 
always divide the main array into it's 2 sub-halves before combining

The Space complexity is O(n)+O(L)+O(R) as we create a additional sub arrays
"""

from datetime import datetime
import math


def merge(data, low, middle_value, high):

    """
    Using the Logic From CLRS
    """

    # Splitting the Main Array into 2 parts,one lesster than the middle value one greater than the middle value
    left_subarray = data[low : middle_value + 1]
    right_subarray = data[middle_value + 1 : high + 1]

    index1, index2 = 0, 0

    k = low

    # Basically Checking if the Index is valid or not
    while index1 < len(left_subarray) and index2 < len(right_subarray):
        # Get the Smallest Element Among both and assign to kth element in data
        if left_subarray[index1] < right_subarray[index2]:
            data[k] = left_subarray[index1]
            index1 += 1

        else:
            data[k] = right_subarray[index2]
            index2 += 1

        k += 1

    # If second Subarray has been exhausted,copy all elements from last index in left subarray
    if index2 == len(right_subarray):
        data[k : high + 1] = left_subarray[index1:]

    # same as above
    if index1 == len(left_subarray):
        data[k : high + 1] = right_subarray[index2:]


def merge_sort(data, low, high):

    """
    Using the Logic From CLRS
    """

    # So This case arises to see which index is bigger,if the index is already lesser,that means the input is sorted(One Elem Case)
    if low < high:
        middle_index = math.floor((low + high) / 2)
        merge_sort(data, low, middle_index)
        merge_sort(data, middle_index + 1, high)
        merge(data, low, middle_index, high)


# Input for Inplace Sort
list_input = list(map(int, input().split()))
start_time = datetime.now()
merge_sort(list_input, 0, len(list_input) - 1)
end_time = datetime.now()
print(list_input, int((end_time - start_time).total_seconds()))
