"""
Here we have used references of the Alrogithm shown in MIT's Introduction to Algorithms and
Geeks for Geeks articles on the same.

https://www.geeksforgeeks.org/insertion-sort/
"""


def insertion_sort(data, ascending=True):

    # Iterate through all items of the list
    for item in range(1, len(data)):
        checking_element = data[item]
        other_index = item - 1

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position

        # For the ascending or the descending case,we just need to change the base condition
        # On the basis of which we do the whole comparision.
        if ascending:

            while other_index >= 0 and checking_element < data[other_index]:
                data[other_index + 1] = data[other_index]
                other_index -= 1

        else:

            while other_index >= 0 and checking_element > data[other_index]:
                data[other_index + 1] = data[other_index]
                other_index -= 1

        # This is done to place the smalles element(I.e the checking at the start of the list
        # Since other index will remain as -1 so at the zeroth element we put the smallest
        # element)
        data[other_index + 1] = checking_element

    return data


data_to_sort = list(map(int, input().split()))

op = insertion_sort(data_to_sort, ascending=True)
print(op)
