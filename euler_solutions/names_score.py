"""
Names Score (Problem 22)

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Takeaway:Use Generator Expressions wherever possible and also look for solutions wherein we do not
need to use lower/Dictionary approach if not required.
"""

import string

alphabet_dictionary = {
    item: index for index, item in enumerate(string.ascii_lowercase, 1)
}

with open(
    "/home/dhruv/Hackerrank-Problem-Solutions/euler_solutions/p022_names.txt", "r"
) as f:
    data = f.readline().split(",")

# Sort the Array in Forward Order
data.sort(reverse=False)

# Solution to manually add the score to the variable

# for index, item in enumerate(data, 1):
#     single_score = sum(alphabet_dictionary[x] for x in item[1:-1].lower())
#     print(single_score, item[1:-1].lower())
#     name_score += single_score * index

# More Efficitent Solution with enumerate to use lesser memory
name_score = sum(
    sum(alphabet_dictionary[x] for x in item[1:-1].lower()) * index
    for index, item in enumerate(data, 1)
)

print(name_score)
