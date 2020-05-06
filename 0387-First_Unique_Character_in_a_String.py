'''
Difficulty: Easy

 Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
'''
from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1

        s_cnt = Counter(s)
        for i, c in enumerate(s):
            if s_cnt[c] == 1:
                return i
        return -1