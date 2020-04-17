'''
Difficulty: Easy

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''


class Solution:
    def reverse(self, x: int) -> int:

        str_int = [int(i) for i in str(abs(x))]

        out = 0

        for e, i in enumerate(str_int):
            out += i * 10 ** e

        if out > 2 ** 31 - 1 or (-1 * out) < -2 ** 31:
            return 0
        if x < 0:
            return out * -1
        else:
            return out