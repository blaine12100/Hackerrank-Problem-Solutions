"""
Here we have used references of the Alrogithm shown in MIT's Introduction to Algorithms and
Geeks for Geeks articles on the same.

https://www.geeksforgeeks.org/selection-sort/
"""


def selection_sort(data, ascending=True):

    # Iterate through all items of the list
    for item in range(len(data)):

        min_index = item

        # For the ascending or the descending case,we just need to change the base condition
        # On the basis of which we do the whole comparision.

        if ascending:
            # Find the Min Element Index
            for j in range(item + 1, len(data)):
                if data[min_index] > data[j]:
                    min_index = j
        else:
            # Find the Max Element Index
            for j in range(item + 1, len(data)):
                if data[min_index] < data[j]:
                    min_index = j

        data[item], data[min_index] = data[min_index], data[item]

    return data


data_to_sort = list(map(int, input().split()))

op = selection_sort(data_to_sort, ascending=False)
print(op)

# Does Not work for Many Cases
#     if ascending:
#         min_in_slice = min(data[item:])
#         index_found = data.index(min_in_slice)
#         if data[item] == data[index_found]:
#             pass
#         else:
#             data[item], data[index_found] = min_in_slice, data[item]

#     else:
#         max_in_slice = max(data[item:])
#         index_found = data.index(max_in_slice)
#         if data[item] == data[index_found]:
#             pass
#         else:
#             data[item], data[index_found] = max_in_slice, data[item]
