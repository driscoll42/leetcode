'''
Difficulty: Medium

Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''

import collections

class Solution:
    def checkValidString(self, s: str) -> bool:
        sList = list(s)
        s_count = collections.Counter(sList)
        curr_paren = 0
        left_list = []
        star_list = []
        for i, x in enumerate(sList):
            if x == "(":
                #print("(")
                curr_paren += 1
                s_count["("] -= 1
                left_list.append(i)
            elif x == ")":
                #print(")", curr_paren,star_list, left_list)
                curr_paren -= 1
                s_count[")"] -= 1
                if curr_paren < 0 and len(star_list) > 0:
                    curr_paren += 1
                    del star_list[-1]
                elif curr_paren < 0:
                    return False
                else:
                    del left_list[-1]
            else:  # "*"
                star_list.append(i)
        # print(curr_paren, star_list, left_list)
        for i, x in enumerate(reversed(left_list)):
            if len(star_list) == 0:
                return False
            else:
                if star_list[-1] > x:
                    del star_list[-1]
                    del left_list[-1]
                    curr_paren -= 1
        # print(curr_paren)
        if curr_paren > 0 or len(left_list) > 0:
            return False
        return True