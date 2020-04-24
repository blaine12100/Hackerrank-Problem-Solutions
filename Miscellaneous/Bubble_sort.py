"""
The Bubble Sort Algorithm is the simplest algorithm in order to sort a list of numbers.In 
this we repeatedly keep on swapping numbers till the preceeding number is less than the 
current number.

We do successive passes for that till the entire list is sorted.Once a single pass finishes
we do the second pass and so on.
"""


def bubble_sort(list_input, ascending=False):
    length_input = len(list_input)

    """For N Passes(Basically the worst case will be to go throught the no of iterations
    as the length of the array to be sorted One way to check the nature of the sorted input will be 
    to store a copy of the last known state of the array and if they both are the same,that means
    the array is sorted"""

    break_loop = False

    for index in range(length_input):

        if break_loop:
            break

        # Re Initialize the Starting and The Ending Indices.
        starting_index = 0
        ending_index = starting_index + 1
        count_swaps = 0

        while ending_index < length_input:

            # Ascending
            if ascending:
                # For Ascending Sort
                if list_input[ending_index] < list_input[starting_index]:
                    list_input[ending_index], list_input[starting_index] = (
                        list_input[starting_index],
                        list_input[ending_index],
                    )

                else:
                    # To count the no of times we have a swap not take place
                    count_swaps += 1

            else:

                # For Descending Sort
                if list_input[ending_index] > list_input[starting_index]:
                    list_input[ending_index], list_input[starting_index] = (
                        list_input[starting_index],
                        list_input[ending_index],
                    )

                else:
                    # To count the no of times we have a swap not take place
                    count_swaps += 1

            """
            Incrementing the indexes to point to the next index to compare the next.
            """

            starting_index = ending_index
            ending_index = starting_index + 1

            # For counting the number of times we can go without swapping
            if count_swaps == length_input - 1:
                break_loop = True

    return list_input


# Driver Code
list_input = list(map(int, input().split()))

op = bubble_sort(list_input)
print(op)
