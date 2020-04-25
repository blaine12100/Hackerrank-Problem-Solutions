"""
For reference
https://www.geeksforgeeks.org/quick-sort/

The time complextiy is the same as Merge sort O(nlogn) but the main 
difference betweeen the 2 is that for linked lists,merge sort is much faster since 
access is randomized and the best time complexity is wthen the pivot is the middle
element and the words is when the pivot is either the last or the first element since
the number  of swaps is greater

Quick Sort is better for arrays since extra space is not required as compared to Merge Sort

The random access is needed because of the Pivot(Rest the access is sequential)
"""

from datetime import datetime
from random import randint


def partition(data, low, high):

    # This function takes last element as pivot, places
    # the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to right
    # of pivot Data is the array,low is starting index and
    # high is the ending index

    # Last Element as Pivot(For all 3 cases the core logic I.E the below piece will remain the same)
    pivot = data[high]
    index = low - 1

    for other in range(low, high):

        if data[other] < pivot:
            index += 1
            data[index], data[other] = data[other], data[index]

    # For putting the pivot at the right place
    data[index + 1], data[high] = data[high], data[index + 1]
    return index + 1


def quick_sort(data, low, high):

    if low < high:

        # So We Recursively Sort the Left Subtree and the Right Subtree based on the ending index
        # lesser than the place at which we partitioned and one index more for the right subtree

        partition_index = partition(data, low, high)
        quick_sort(data, low, partition_index - 1)
        quick_sort(data, partition_index + 1, high)


# Input for Inplace Sort
list_input = list(map(int, input().split()))
start_time = datetime.now()
quick_sort(list_input, 0, len(list_input) - 1)
end_time = datetime.now()
print(list_input, int((end_time - start_time).total_seconds()))
