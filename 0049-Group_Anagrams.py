'''
Difficulty: Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        inner = {}
        alpha = {'a': 2,
                 'b': 3,
                 'c': 5,
                 'd': 7,
                 'e': 11,
                 'f': 13,
                 'g': 17,
                 'h': 19,
                 'i': 23,
                 'j': 29,
                 'k': 31,
                 'l': 37,
                 'm': 41,
                 'n': 43,
                 'o': 47,
                 'p': 53,
                 'q': 59,
                 'r': 61,
                 's': 67,
                 't': 71,
                 'u': 73,
                 'v': 79,
                 'w': 83,
                 'x': 89,
                 'y': 97,
                 'z': 101}

        for x in strs:
            total = 1
            for i in x:
                total *= alpha[i]
            if total in inner.keys():
                inner[total].append(x)
            else:
                inner[total] = [x]
            print(total)

        output = []
        for value in inner.values():
            output.append(value)

        return output