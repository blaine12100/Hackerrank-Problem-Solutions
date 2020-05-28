"""
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1. 

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

"""

from collections import OrderedDict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Initial Dictionary Approach
        new_dict = OrderedDict()
        first_common = False
        first_common_key = 0
        for item in s:
            new_dict[item] = new_dict.get(item, 0) + 1
        # print(new_dict)
        for key, value in new_dict.items():
            if value == 1:
                first_common_key = key
                first_common = True
                break

        if first_common:
            return list(s).index(first_common_key)
        else:
            return -1

        # Better Solution

        for index, item in enumerate(s):
            if new_dict[item] == 1:
                first_common_key = index
                first_common = True
                break

        if first_common:
            return first_common_key
        else:
            return -1
